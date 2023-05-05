import Data
from mtranslate import translate
while True:
    generated_text = Data.generate_text (translate(input(">>>"), to_language='en'))
    print(translate(generated_text, to_language='ko'))