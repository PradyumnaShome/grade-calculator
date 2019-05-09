import yaml
import sys
import os
import pprint


def get_course_info(yaml_path):
    with open(yaml_path, "r") as file:
        return yaml.load(file.read(), Loader=yaml.Loader)


def calculate_assignment_grade(assignment):
    count_drops = assignment["drops"]
    scores_with_drops = sorted(assignment["scores"])[count_drops:]
    assignment_average = sum(scores_with_drops) / (len(scores_with_drops))
    print(f"Average for {assignment['name']} = {assignment_average}.")
    return assignment_average


def calculate_final_grade(course_info):
    final_grade = 0.0
    for assignment in course_info["assignments"]:
        assignment_average = calculate_assignment_grade(assignment)
        final_grade += assignment_average / 100.0 * assignment["points"]
    return final_grade


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Must provide path to grades YAML.", file=sys.stderr)
        sys.exit(os.EX_USAGE)

    yaml_path = sys.argv[1]
    course_info = get_course_info(yaml_path)
    final_grade = calculate_final_grade(course_info)
    print(f"Your final grade for {course_info['class']} is: {final_grade}.")
