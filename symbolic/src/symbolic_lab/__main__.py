from symbolic_lab.pipeline import run_prototype


def main() -> None:
    outputs = run_prototype()
    print("symbolic 共通テンプレの出力が完了しました")
    print(f"特徴量表: {outputs['table']}")
    print(f"特徴量辞書: {outputs['dictionary']}")
    print(f"レポート: {outputs['report']}")


if __name__ == "__main__":
    main()
