import json
import os
import pandas as pd
import argparse


def report_llms_accuracies(evaluation_directory,
                           row_names,
                           output_filename):

    entries = os.listdir(evaluation_directory)

    dirs = sorted(
        [name for name in entries if os.path.isdir(
            os.path.join(evaluation_directory, name))],
        key=lambda x: int(x))

    directory_scores = []
    for dir in dirs:
        result_directory = os.path.join(evaluation_directory, dir)
        files = sorted(
            f for f in os.listdir(result_directory)
            if os.path.isfile(os.path.join(result_directory, f))
            and 'evaluation-results' in f
        )

        column_names = ['abstention', 'contradiction_resolution', 'event_ordering', 'information_extraction', 'instruction_following',
                        'knowledge_update', 'multi_session_reasoning', 'preference_following', 'summarization', 'temporal_reasoning']

        file_scores = []
        for file in files:
            if file in row_names:
                evaluation_file_path = os.path.join(result_directory, file)
                with open(evaluation_file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                scores = []
                for key in data.keys():
                    objects = data[key]
                    score = 0
                    for object in objects:
                        if key == "event_ordering":
                            score += object['tau_norm']
                        else:
                            score += object['llm_judge_score']

                    scores.append(score/len(objects))

                if len(scores) != 10:
                    print("File length is not correct")
                file_scores.append(scores)

        if file_scores:
            directory_scores.append(file_scores)

    N = len(directory_scores)
    M = len(directory_scores[0])
    K = len(directory_scores[0][0])

    avg_scores = [
        [
            sum(directory_scores[n][m][k] for n in range(N)) / N
            for k in range(K)
        ]
        for m in range(M)
    ]

    df = pd.DataFrame(avg_scores, columns=column_names)
    df.insert(0, "RowName", row_names)

    output_address = os.path.join(evaluation_directory, output_filename)
    df.to_excel(output_address, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate LLM evaluation accuracy reports."
    )

    parser.add_argument(
        "--evaluation_directory",
        type=str,
        required=True,
        help="Path to the main directory containing evaluation results."
    )

    parser.add_argument(
        "--row_names",
        nargs="+",
        required=True,
        help="List of filenames (without paths) to include as rows in the report."
    )

    parser.add_argument(
        "--output_filename",
        type=str,
        default="llm_evaluation_report.xlsx",
        help="Name of the output Excel file."
    )

    args = parser.parse_args()

    report_llms_accuracies(
        evaluation_directory=args.evaluation_directory,
        row_names=args.row_names,
        output_filename=args.output_filename
    )
    