class ShardRouter:
    """
    A router to control all database operations for sharded User model.
    """

    def db_for_read(self, model, **hints):
        if model.__name__ == 'User':
            user_id = hints.get('user_id')
            if user_id is not None:
                return self.get_shard(user_id)
        return None

    def db_for_write(self, model, **hints):
        if model.__name__ == 'User':
            user_id = hints.get('user_id')
            if user_id is not None:
                return self.get_shard(user_id)
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'user':
            return db in ('shard_1', 'shard_2', 'shard_3')
        return None

    def get_shard(self, user_id):
        # Hash function: user_id % 3
        shard_number = user_id % 3
        return f'shard_{shard_number + 1}'
