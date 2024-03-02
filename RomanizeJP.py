def convert_to_japanese(input_str):
    japanese_mapping = {
    'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お',
    'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
    'sa': 'さ', 'si': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
    'ta': 'た', 'ti': 'ち', 'tu': 'つ', 'te': 'て', 'to': 'と',
    'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
    'ha': 'は', 'hi': 'ひ', 'hu': 'ふ', 'he': 'へ', 'ho': 'ほ',
    'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
    'ya': 'や', 'yi': 'い', 'yu': 'ゆ', 'ye': 'いぇ', 'yo': 'よ',
    'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
    'wa': 'わ', 'wi': 'うぃ', 'wu': 'う', 'we': 'うぇ', 'wo': 'を',
    'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
    'za': 'ざ', 'zi': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
    'da': 'だ', 'di': 'ぢ', 'du': 'づ', 'de': 'で', 'do': 'ど',
    'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
    'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',
    'kwa': 'くぁ', 'kwi': 'ｋうぃ', 'kwu': 'ｋうぃ', 'kwe': 'ｋうぇ', 'kwo': 'ｋを',
    'sha': 'しゃ', 'shi': 'し', 'shu': 'しゅ', 'she': 'しぇ', 'sho': 'しょ',
    'cha': 'ちゃ', 'chi': 'ち', 'chu': 'ちゅ', 'che': 'しぇ', 'cho': 'ちょ',
    'tsa': 'つぁ', 'tsi': 'つぃ', 'tsu': 'つ', 'tse': 'つぇ', 'tso': 'つぉ',
    'fa': 'ふぁ', 'fi': 'ふぃ', 'fu': 'ふ', 'fe': 'ふぇ', 'fo': 'ふぉ',
    'ja': 'じゃ', 'ji': 'じ', 'ju': 'じゅ', 'je': 'じぇ', 'jo': 'じょ',
    'va': 'ヴぁ', 'vi': 'ヴぃ', 'vu': 'ヴ', 've': 'ヴぇ', 'vo': 'ヴぉ',
    'kya': 'きゃ', 'kyi': 'きぃ', 'kyu': 'きゅ', 'kye': 'きぇ', 'kyo': 'きょ',
    'nya': 'にゃ', 'nyi': 'にぃ', 'nyu': 'にゅ', 'nye': 'にぇ', 'nyo': 'にょ',
    'hya': 'ひゃ', 'hyi': 'ひぃ', 'hyu': 'ひゅ', 'hye': 'ひぇ', 'hyo': 'ひょ',
    'mya': 'みゃ', 'myi': 'みぃ', 'myu': 'みゅ', 'mye': 'みぇ', 'myo': 'みょ',
    'rya': 'りゃ', 'ryi': 'りぃ', 'ryu': 'りゅ', 'rye': 'りぇ', 'ryo': 'りょ',
    'gya': 'ぎゃ', 'gyi': 'ぎぃ', 'gyu': 'ぎゅ', 'gye': 'ぎぇ', 'gyo': 'ぎょ',
    'bya': 'びゃ', 'byi': 'びぃ', 'byu': 'びゅ', 'bye': 'びぇ', 'byo': 'びょ',
    'pya': 'ぴゃ', 'pyi': 'ぴぃ', 'pyu': 'ぴゅ', 'pye': 'ぴぇ', 'pyo': 'ぴょ',
    'tha': 'てゃ', 'thi': 'てぃ', 'thu': 'てゅ', 'the': 'てぇ', 'tho': 'てょ',
    'qa': 'くぁ', 'qi': 'くぃ', 'qu': 'く', 'qe': 'くぇ', 'qo': 'くぉ',
    'tya': 'ちゃ', 'tyi': 'ちぃ', 'tyu': 'ちゅ', 'tye': 'ちぇ', 'tyo': 'ちょ',
    'gwa': 'ぐぁ', 'gwi': 'ぐぃ', 'gwu': 'ぐぅ', 'gwe': 'ぐぇ', 'gwo': 'ぐぉ',
    'sya': 'しゃ', 'syi': 'しぃ', 'syu': 'しゅ', 'sye': 'しぇ', 'syo': 'しょ',
    'zya': 'じゃ', 'zyi': 'じぃ', 'zyu': 'じゅ', 'zye': 'じぇ', 'zyo': 'じょ',
    'twa': 'とぁ', 'twi': 'とぃ', 'twu': 'とぅ', 'twe': 'とぇ', 'two': 'とぉ',
    'dya': 'ぢゃ', 'dyi': 'ぢぃ', 'dyu': 'ぢゅ', 'dye': 'ぢぇ', 'dyo': 'ぢょ',
    'dha': 'でゃ', 'dhi': 'でぃ', 'dhu': 'でゅ', 'dhe': 'でぇ', 'dho': 'でょ',
    'fwa': 'ふぁ', 'fwi': 'ふぃ', 'fwu': 'ふぅ', 'fwe': 'ふぇ', 'fwo': 'ふぉ',
    'wha': 'うぁ', 'whi': 'うぃ', 'whu': 'う', 'whe': 'うぇ', 'who': 'うぉ',
    'qwa': 'くぁ', 'qwi': 'くぃ', 'qwu': 'くぅ', 'qwe': 'くぇ', 'qwo': 'くぉ',
    'la': 'ぁ', 'li': 'ぃ', 'lu': 'ぅ', 'le': 'ぇ', 'lo': 'ぉ',
    'xa': 'ぁ', 'xi': 'ぃ', 'xu': 'ぅ', 'xe': 'ぇ', 'xo': 'ぉ',
    'n': 'ん',
    'b': 'ｂ', 'c': 'ｃ', 'd': 'ｄ', 'f': 'ｆ', 'g': 'ｇ',
    'h': 'ｈ', 'j': 'ｊ', 'k': 'ｋ', 'l': 'ｌ', 'm': 'ｍ',
    'p': 'ｐ', 'q': 'ｑ', 'r': 'ｒ', 's': 'ｓ', 't': 'ｔ',
    'v': 'ｖ', 'w': 'ｗ', 'x': 'ｘ', 'y': 'ｙ', 'z': 'ｚ',
    }

    output_str = ''
    num_chars = len(input_str)
    i = num_chars
    while i > 0:
        if i >= 3 and input_str[num_chars - i:num_chars - i + 3] in japanese_mapping:
            output_str += japanese_mapping[input_str[num_chars - i:num_chars - i + 3]]
            i -= 3
        elif i >= 2 and input_str[num_chars - i:num_chars - i + 2] in japanese_mapping:
            output_str += japanese_mapping[input_str[num_chars - i:num_chars - i + 2]]
            i -= 2
        elif input_str[num_chars - i] in japanese_mapping:
            output_str += japanese_mapping[input_str[num_chars - i]]
            if i == 1 and input_str[num_chars - i] == 'n':
                # print("禁則処理:", input_str[num_chars - i])
                output_str = output_str[:-1] + 'ｎ'
            i -= 1
        else:
            print("未登録の単語が使われています:", input_str, input_str[num_chars - i])
            i -= 1
    return output_str

def main():
    input_file_path = input("ファイルのパスを入力してください：")
    # output_file_path = input("保存先のファイルのパスを入力してください：")
    output_file_path = "output.txt"
    
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()
    
    output_str = ''
    for line in lines:
        line = line.strip()  # 改行文字を取り除く
        output_str += convert_to_japanese(line) + '\n'
    
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(output_str)

    print("結果をファイルに保存しました。")

if __name__ == "__main__":
    main()
