# https://school.programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    playlist = {}
    for genre in genres:
        playlist[genre] = {
            'total': 0,
            'songs': {
                # 'id': 'play'
            }
        }

    for i in range(len(genres)):
        playlist[genres[i]]['total'] += plays[i]
        playlist[genres[i]]['songs'][i] = plays[i]

    playlist = list(sorted(playlist.items(), key=lambda item: item[1]['total'], reverse=True))
    answer = []
    for genre in playlist:
        best_songs = list(sorted(genre[1]['songs'].items(), key=lambda item: item[1], reverse=True))
        limit = 0
        while len(best_songs) > 0:
            answer.append(best_songs.pop(0)[0])
            limit += 1
            if limit > 1:
                break

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
