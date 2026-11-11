# Graph Report - Learning  (2026-11-12)

## Corpus Check
- В структурный анализ включено файлов исходного кода: 8. Сторонние зависимости, документация и файлы окружения исключены.

## Summary
- 57 nodes · 72 edges · 7 communities (2 shown, 5 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- sqlOptimization.py
- RedisCache.py
- avroproducer.py
- update_product
- rabbitconsumer.py
- confluent_kafka
- get_users_with_orders

## God Nodes (most connected - your core abstractions)
1. `Base` - 4 edges
2. `update_product()` - 4 edges
3. `OrderSchema` - 3 edges
4. `UserSchema` - 3 edges
5. `Base` - 3 edges
6. `ProductSchema` - 3 edges
7. `ProductUpdateSchema` - 3 edges
8. `get_product()` - 3 edges
9. `consumer_callback()` - 3 edges
10. `get_users_with_orders()` - 3 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (7 total, 5 thin omitted)

### Community 0 - "sqlOptimization.py"
Cohesion: 0.24
Nodes (7): Base, Order, OrderSchema, Config, User, UserSchema, Config

### Community 3 - "update_product"
Cohesion: 0.22
Nodes (5): get_product(), ProductSchema, Config, ProductUpdateSchema, update_product()

## Knowledge Gaps
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_users_with_orders()` connect `get_users_with_orders` to `sqlOptimization.py`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **Why does `update_product()` connect `update_product` to `RedisCache.py`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._