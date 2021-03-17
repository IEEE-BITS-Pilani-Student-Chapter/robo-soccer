from gym.envs.registration import register

register(
    id='Robosoccer2v2-v1',
    entry_point='robo_soccer.envs_v1:Robosoccer',
    kwargs={'number_of_player': 2},
)

register(
    id='Robosoccer5v5-v1',
    entry_point='robo_soccer.envs_v1:Robosoccer',
    kwargs={'number_of_player': 5},
)

register(
    id='Robosoccer-v1',
    entry_point='robo_soccer.envs_v1:Robosoccer',
    kwargs={'number_of_player': 10},
)
