def solution(record):
  name = {}
  answer = []

  for re in record:
    split_arr = re.split(" ")
    if split_arr[0] == "Change":
      name[split_arr[1]] = split_arr[2]
    elif split_arr[0] == "Enter":
      name[split_arr[1]] = split_arr[2]

  for re in record:
    split_arr = re.split(" ")
    if split_arr[0] == "Enter":
      answer.append(f"{name[split_arr[1]]}님이 들어왔습니다.")
    if split_arr[0] == "Leave":
      answer.append(f"{name[split_arr[1]]}님이 나갔습니다.")

  return answer