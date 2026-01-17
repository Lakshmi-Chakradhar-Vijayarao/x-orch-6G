from experiments.run_baselines import run_baselines
from experiments.run_ppo import run_ppo_training
from experiments.run_marl import run_marl
from experiments.run_no_op_ablation import run_ablation


def main():
    print("\n=== FULL DEMO ===")

    run_baselines()
    run_ppo_training()
    run_marl()

    run_ablation(True)
    run_ablation(False)


if __name__ == "__main__":
    main()
