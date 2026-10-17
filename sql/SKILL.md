---
name: sql
description: Write and run efficient SQL when query latency, database load, or scan cost matters. Use for database queries and slow-query tuning that need schema-aware, cost-aware decisions.
---

# SQL

Write SQL that returns the requested result with reasonable latency and database work. Keep the query correct first, then use the database's own evidence to reduce work. Do not assume that a shorter query is a faster one.

## Learn the database before writing

- Identify the engine and version, the environment (production, replica, warehouse, or local), and the available query and cost limits. Use the dialect and planning tools for that engine.
- Inspect only the relevant schema: table relationships and keys, indexes or clustering and partitioning, views, table sizes, and available row-count and column-distribution statistics. Reuse known metadata. Prefer catalogs and existing telemetry over exploratory full-table `COUNT(*)` queries.
- Establish the result's grain, filters, time range, expected output size, and whether the user needs exact or approximate results. If there is no database access, do not invent schema or cardinalities; state the assumptions behind the SQL.

## Make the work proportional to the answer

- Select the columns needed. Apply selective predicates and partition filters where the engine can use them. Keep predicates on indexed or partitioned columns usable by the optimizer when possible.
- Join on the intended keys and reason about one-to-many fanout before adding joins. Aggregate at the required grain when that preserves the answer. Avoid accidental cross joins, repeated large scans, unnecessary `DISTINCT`, and global sorts.
- Use `LIMIT` or pagination to bound returned rows when appropriate, but do not treat `LIMIT` as proof that scanning, joining, grouping, or sorting is cheap.
- Let the optimizer choose among plausible plans unless measured evidence supports a hint or forced join order. If estimates look wrong, investigate stale statistics, skew, correlated columns, and missing access paths before rewriting SQL blindly.

## Check cost before execution

- Use an engine-native plan or dry run that does not execute the query, when available. For example, PostgreSQL and DuckDB have plain `EXPLAIN`; BigQuery has dry runs. Inspect expected rows at scans and joins, bytes or partitions read, large sorts or aggregates, and likely spill or fanout. Treat cost units and row estimates as estimates, not elapsed-time promises.
- Compare the expected work with the user's goal, database size, and any existing budget or workload limits. If the plan looks excessive or uncertain, narrow or reshape the query and inspect the new plan. Do not launch a costly query merely to see whether it finishes.
- If no useful estimate is available and the likely work is large, provide the proposed SQL and the missing cost check instead of executing blindly.
- `EXPLAIN ANALYZE` and equivalent actual-plan tools execute the statement. Use them only after the same cost check and only when the extra run is justified. They can have side effects for writes.

## Finish and learn from the run

- If execution is part of the task and the query has passed the cost check, run it and wait for the result. Do not start speculative queries with a plan to cancel them, abandon an in-flight query because a different answer seems more interesting, or rerun one without checking whether the first job is still active. Consume or save the result so the work answers the user's question.
- Respect an explicit user cancellation, server-enforced limits, and operational safety controls. If a query fails or is interrupted, report that no completed result was obtained; inspect its status before deciding whether a revised run is worthwhile.
- Compare completed-run metrics with the estimate when the database provides them. If the query was slow, use the actual bottleneck to revise the SQL or recommend a schema or statistics change. Do not change indexes, statistics, or production settings as a side effect of query writing without authorization.
- Return the SQL, the relevant assumptions, and a concise account of the plan or observed work. If cost could not be checked, say so and distinguish a proposed query from a verified fast one.
