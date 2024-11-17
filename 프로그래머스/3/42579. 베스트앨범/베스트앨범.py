def solution(genres, plays):
  genres_dict = {}
  plays_dict = {}
  for i, genre in enumerate(genres):
    play = plays[i]
    if genre not in genres_dict:
      genres_dict[genre] = []
      plays_dict[genre] = 0
    genres_dict[genre].append((i, play))  
    plays_dict[genre] += play

  sorted_genres = sorted(plays_dict.items(), key=lambda x:x[1], reverse=True)
  answer = [] 
  for genre, _ in sorted_genres:
    sorted_songs = sorted(genres_dict[genre], key=lambda x: (-x[1], x[0]))
    answer.extend([i for i, _ in sorted_songs[:2]])
  print(answer)
  return answer