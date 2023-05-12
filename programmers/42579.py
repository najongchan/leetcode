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

    sorted_playlist = list(sorted(playlist.items(), key=lambda item: item[1]['total'], reverse=True))
    answer = []
    for x in sorted_playlist:
        best_songs = list(sorted(x[1]['songs'].items(), key=lambda item: item[1], reverse=True))[:2]
        for song in best_songs:
            answer.append(song[0])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop", "hiphop"], [500, 600, 150, 800, 2500,10]))
