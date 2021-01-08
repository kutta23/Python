# 포매팅(formatting)

# positional formatting -> 순서대로 
print('''안녕하세요 오늘 오전 낮 기온은 {}이고,
오후에는 {}입니다'''.format("11도","20도"))

# named placeholder 
print('''안녕하세요 오늘 오전 낮 기온은 {오전기온}이고,
오후에는 {오후기온}입니다'''.format(오전기온="11도",오후기온="20도"))