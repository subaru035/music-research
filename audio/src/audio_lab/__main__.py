from audio_lab.pipeline import run_prototype


def main() -> None:
    outputs = run_prototype()
    print("audio prototype finished")
    print(f"table: {outputs['table']}")
    print(f"report: {outputs['report']}")


if __name__ == "__main__":
    main()

