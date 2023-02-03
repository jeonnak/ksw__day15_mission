def find_and_insert_data(pokemon, hp):
	find_pos = -1  # 새 포켓몬의 위치를 -1로 설정
	for i in range(len(pokemons)) :  # 포켓몬의 수만큼 for문을 실행시킬 것.
		pair = pokemons[i]
		if hp >= pair[1] :  # 새로온 포켓몬의 hp가 pokemons 리스트 내의 i번째 포켓몬의 hp보다 높다면 hp의 위치는 바로 그자리. hp가 더 큰 포켓몬이 더 왼쪽
			find_pos = i
			break
	if find_pos == -1 :  # 만약 새로 온 포켓몬이 hp가 가장 적다면 위치가 -1에 머물 것이다. 그렇다면
		find_pos = len(pokemons) #새 포켓몬의 자리는 맨 끝자리.

	insert_data(find_pos, [pokemon, hp])  # 새로온 포켓몬을 find_pos의 위치에 [pokemon,hp] 형식으로 넣어주겠다.


def insert_data(position, pokemon):
	if position < 0 or position > len(pokemons):
		print("데이터를 삽입할 범위를 벗어났습니다.")
		return

	pokemons.append(None)	# 빈 칸을 추가해 준다.
	p_len = len(pokemons)		# 배열의 현재 크기

	for i in range(p_len - 1, position, -1):
		pokemons[i] = pokemons[i - 1]
		pokemons[i - 1] = None

	pokemons[position] = pokemon


pokemons = [['피카츄', 900], ['꼬부기', 600], ['라이츄', 400], ['또가스', 300]]



if __name__ == "__main__":

	while True:
		data = input("가랏 포켓몬! : ")
		count = int(input("투입시킬 포켓몬의 체력은? : "))
		find_and_insert_data(data, count)
		print(pokemons)