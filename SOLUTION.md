# Solution Steps

1. Locate the products table SQLAlchemy model (Product).

2. Declare a composite B-Tree index on (category_id, brand_id) in the Product model using SQLAlchemy's Index.

3. If using Alembic for migrations, generate a migration file to add the composite index on (category_id, brand_id) to the products table in the database.

4. In the migration, use op.create_index() with the desired columns. Add corresponding code for downgrade to remove the index.

5. Apply (run) the migration to update the production and test databases.

6. (Optional, post-deploy) Use EXPLAIN on queries filtering by category_id and brand_id to verify that the index is being used.

7. No changes are needed to endpoints, query logic, or validation models.

