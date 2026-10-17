---
name: cpp
description: Write, review, and refactor C++17-or-newer code with compact functions, request-specific handlers, liberal but clear auto, immutable values, and named file-local string constants. Use for C++ implementation and code review; follow the project's required standard and toolchain.
---

# C++

Write direct, modern C++ that is easy to trace. Apply the user's conventions below when editing C++ code. They take precedence over generic style guides; preserve an existing public API, ABI, or required project convention when changing it would exceed the task.

## Structure functions by responsibility

- Keep each function focused on one logical operation. A listener or entry point accepts work and dispatches it. Give each distinct API request or route its own handler; a handler owns that request's behavior and calls other functions only for substantial, named operations.
- Avoid a one-caller helper whose body is roughly one to four substantive lines. Put that logic in its caller when doing so keeps the caller clear. Do not count braces, wrapping, or formatting as complexity. A distinct request handler, callback required by an interface, resource lifetime boundary, or operation with a meaningful independent contract can remain a function even if short.
- Do not turn this preference into a giant handler. Split a function when it handles unrelated decisions, has separate domain steps worth naming, or is hard to understand without holding too much state in mind. Remove trivial pass-through layers.

## Constants and type deduction

- Define hard-coded application string values at the top of their owning `.cpp` file, after includes. Group related constants. Use file-local `static const std::string` and `UPPER_SNAKE_CASE` names by default; avoid scattering string literals through the implementation. Keep constants in the narrowest file that uses them, rather than making a shared constants module for one file.
- When the code only needs a non-owning view of a literal, `static constexpr std::string_view` is also acceptable. It keeps the same file-local, immutable, uppercase convention and avoids constructing a global `std::string`. Check the lifetime before storing a view. Put genuinely shared constants in a suitable header using the project's linkage conventions.
- Make values that do not change `const`, including local strings and read-only references; use `constexpr` for compile-time values. Make non-mutating member functions `const`. Do not add `const` to a local returned by value if it would inhibit a needed move.
- Prefer `auto` for initialized local variables, iterators, structured bindings, and range loops. Keep `const` and `&` where needed: `const auto&` must not silently become a copy. Spell out types for interfaces, intentional conversions, ownership or lifetime decisions, and cases where deduction hides an important type.

```cpp
// After includes, in the .cpp file that owns these routes.
static const std::string GET_USERS_PATH{"/users"};
static const std::string CREATE_USER_PATH{"/users/create"};
static const std::string NOT_FOUND_MESSAGE{"Not found"};
static constexpr int NOT_FOUND_STATUS{404};

int main() {
    auto server = Server{};
    server.listen([](const Request& request) -> Response {
        if (request.path == GET_USERS_PATH) return handle_get_users(request);
        if (request.path == CREATE_USER_PATH) return handle_create_user(request);
        return Response{NOT_FOUND_STATUS, NOT_FOUND_MESSAGE};
    });
}
```

`Server`, `Request`, `Response`, and the handlers stand for the project's own types and functions. Keep the route handlers even when one currently has only a few lines: each is the entry point for a distinct request.

## Modern C++ baseline

- Check the project's C++ standard, compiler, standard library, and existing `.clang-format` before choosing features. Use C++17 facilities such as `std::optional`, `std::variant`, `std::string_view`, structured bindings, and `if constexpr` when useful. Use `std::span`, ranges, and concepts only with C++20 support; use `std::expected` only with C++23 library support. Do not raise the language standard merely to shorten code.
- Use RAII for files, locks, sockets, and memory. Prefer scoped values and the Rule of Zero. Use `std::unique_ptr` for necessary exclusive heap ownership; use `std::shared_ptr` only for actual shared ownership. Raw pointers and references can express non-owning access. Avoid naked `new`/`delete` in application code.
- Express invalid states with types where practical: `enum class`, suitable value types, and `std::optional` or `std::expected` when their meanings fit. Return results rather than using output parameters. Use the project's established error strategy at API boundaries; do not mix exceptions and status returns arbitrarily.
- Use standard containers and algorithms before hand-written memory management. Treat `std::string_view` and `std::span` as borrowed views whose source must outlive them. Avoid unchecked narrowing, C-style casts, and macros for constants.
- Keep validation at input and ownership boundaries. Avoid repeating the same check through every internal layer. Measure before claiming an optimization; prefer clear data flow and predictable ownership over speculative cleverness.

## Verify relevant changes

- Build with the project's required standard and warnings. Use its formatter and focused static analysis when configured. For CMake changes, express language requirements on the relevant target rather than changing every target globally.
- Run the affected tests. For changes involving memory or concurrency, use available AddressSanitizer, UndefinedBehaviorSanitizer, or ThreadSanitizer configurations when practical. Check error paths and resource cleanup, not only the successful path.

## Source guidance

- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines): single-operation functions, RAII, constness, return values, and judicious `auto`.
- [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html): `constexpr` string views for file-scope literals and explicit `const` in interfaces. Its naming rules do not override the conventions above.
- [Clang tooling](https://clang.llvm.org/extra/clang-tidy/index.html) and [sanitizers](https://clang.llvm.org/docs/AddressSanitizer.html): static checks and memory-error detection.
- [CMake target compile features](https://cmake.org/cmake/help/latest/guide/tutorial/In-Depth%20CMake%20Target%20Commands.html): target-specific C++ standard requirements.
