keyboard = {"+": chr(33), ".": chr(34), "๒": chr(35), "๓": chr(36), "๔": chr(37), 
            "฿": chr(38), "ง": chr(39), "๖": chr(40), "๗": chr(41), "๕": chr(42), 
            "๙": chr(43), "ม": chr(44), "ข": chr(45), "ใ": chr(46), "ฝ": chr(47), 
            "จ": chr(48), "ๅ": chr(49), "/": chr(50), "-": chr(51), "ภ": chr(52), 
            "ถ": chr(53), "ึ": chr(54), "ึ": chr(55), "ค": chr(56), "ต": chr(57), 
            "ซ": chr(58), "ว": chr(59), "ฒ": chr(60), "ช": chr(61), "ฬ": chr(62), 
            "ฦ": chr(63), "๑": chr(64), "ฤ": chr(65), "ฺ": chr(66), "ฉ": chr(67), 
            "ฏ": chr(68), "ฎ": chr(69), "โ": chr(70), "ฌ": chr(71), "็": chr(72), 
            "ณ": chr(73), "๋": chr(74), "ษ": chr(75), "ศ": chr(76), "?": chr(77), 
            "์": chr(78), "ฯ": chr(79), "ญ": chr(80), "๐": chr(81), "ฑ": chr(82), 
            "ฆ": chr(83), "ธ": chr(84), "": chr(85), "ฮ": chr(86), '"': chr(87), 
            ")": chr(88), "ํ": chr(89), "(": chr(90), "บ": chr(91), "ฃ": chr(92), 
            "ล": chr(93), "ุ": chr(94), "๘": chr(95), "_": chr(96), "ฟ": chr(97), 
            "ิ": chr(98), "แ": chr(99), "ก": chr(100), "ำ": chr(101), "ด": chr(102), 
            "เ": chr(103), "": chr(104), "ร": chr(105), "่": chr(106), "า": chr(107), 
            "ส": chr(108), "ท": chr(109), "ื": chr(110), "น": chr(111), "ย": chr(112), 
            "ๆ": chr(113), "พ": chr(114), "ห": chr(115), "ะ": chr(116), "ี": chr(117), 
            "อ": chr(118), "ไ": chr(119), "ป": chr(120), "ั": chr(121), "ผ": chr(122), 
            "ฐ": chr(123), "ฅ": chr(124), ",": chr(125), "%": chr(126)}

import json

with open('BackUp/keybaordThai.json', 'w') as json_file:
    json.dump(keyboard, json_file)