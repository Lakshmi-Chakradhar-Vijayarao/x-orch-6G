from experiments.run_baselines import run_baselines
from experiments.run_ppo import run_ppo_training
from experiments.run_marl import run_marl


def main():
    print("\n=== QUICK DEMO ===")

    run_baselines()
    run_ppo_training(total_timesteps=5_000)
    run_marl()


if __name__ == "__main__":
    main()
