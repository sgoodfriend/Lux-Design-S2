from luxai_s2.config import EnvConfig
def is_day(config: EnvConfig, env_step):
    return env_step % config.CYCLE_LENGTH < config.DAY_LENGTH