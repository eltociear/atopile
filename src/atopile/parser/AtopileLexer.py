# Generated from AtopileLexer.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


if __name__ is not None and "." in __name__:
    from .AtopileLexerBase import AtopileLexerBase
else:
    from AtopileLexerBase import AtopileLexerBase

def serializedATN():
    return [
        4,0,68,667,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,
        91,7,91,2,92,7,92,2,93,7,93,2,94,7,94,1,0,1,0,3,0,194,8,0,1,1,1,
        1,1,1,3,1,199,8,1,1,2,1,2,1,2,1,2,3,2,205,8,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,3,7,238,8,7,1,7,1,7,3,
        7,242,8,7,1,7,3,7,245,8,7,3,7,247,8,7,1,7,1,7,1,8,1,8,5,8,253,8,
        8,10,8,12,8,256,9,8,1,9,1,9,1,9,1,9,1,9,3,9,263,8,9,1,9,1,9,3,9,
        267,8,9,1,10,1,10,1,10,1,10,1,10,3,10,274,8,10,1,10,1,10,3,10,278,
        8,10,1,11,1,11,5,11,282,8,11,10,11,12,11,285,9,11,1,11,4,11,288,
        8,11,11,11,12,11,289,3,11,292,8,11,1,12,1,12,1,12,4,12,297,8,12,
        11,12,12,12,298,1,13,1,13,1,13,4,13,304,8,13,11,13,12,13,305,1,14,
        1,14,1,14,4,14,311,8,14,11,14,12,14,312,1,15,1,15,3,15,317,8,15,
        1,16,1,16,3,16,321,8,16,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,
        1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,23,1,23,1,24,
        1,24,1,25,1,25,1,25,1,26,1,26,1,27,1,27,1,27,1,28,1,28,1,28,1,29,
        1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,32,1,33,1,33,1,33,1,34,1,34,
        1,35,1,35,1,36,1,36,1,37,1,37,1,38,1,38,1,38,1,39,1,39,1,40,1,40,
        1,40,1,41,1,41,1,41,1,42,1,42,1,43,1,43,1,44,1,44,1,44,1,45,1,45,
        1,45,1,46,1,46,1,46,1,47,1,47,1,47,1,48,1,48,1,48,1,49,1,49,1,50,
        1,50,1,50,1,51,1,51,1,51,1,52,1,52,1,52,1,53,1,53,1,53,1,54,1,54,
        1,54,1,55,1,55,1,55,1,56,1,56,1,56,1,57,1,57,1,57,1,58,1,58,1,58,
        1,59,1,59,1,59,1,60,1,60,1,60,1,60,1,61,1,61,1,61,1,61,1,62,1,62,
        1,62,1,62,1,63,1,63,1,63,1,63,1,64,1,64,1,64,3,64,457,8,64,1,64,
        1,64,1,65,1,65,1,66,1,66,1,66,5,66,466,8,66,10,66,12,66,469,9,66,
        1,66,1,66,1,66,1,66,5,66,475,8,66,10,66,12,66,478,9,66,1,66,3,66,
        481,8,66,1,67,1,67,1,67,1,67,1,67,5,67,488,8,67,10,67,12,67,491,
        9,67,1,67,1,67,1,67,1,67,1,67,1,67,1,67,1,67,5,67,501,8,67,10,67,
        12,67,504,9,67,1,67,1,67,1,67,3,67,509,8,67,1,68,1,68,3,68,513,8,
        68,1,69,1,69,1,70,1,70,1,70,1,70,3,70,521,8,70,1,71,1,71,1,72,1,
        72,1,73,1,73,1,74,1,74,1,75,1,75,1,76,3,76,534,8,76,1,76,1,76,1,
        76,1,76,3,76,540,8,76,1,77,1,77,3,77,544,8,77,1,77,1,77,1,78,4,78,
        549,8,78,11,78,12,78,550,1,79,1,79,4,79,555,8,79,11,79,12,79,556,
        1,80,1,80,3,80,561,8,80,1,80,4,80,564,8,80,11,80,12,80,565,1,81,
        1,81,1,81,5,81,571,8,81,10,81,12,81,574,9,81,1,81,1,81,1,81,1,81,
        5,81,580,8,81,10,81,12,81,583,9,81,1,81,3,81,586,8,81,1,82,1,82,
        1,82,1,82,1,82,5,82,593,8,82,10,82,12,82,596,9,82,1,82,1,82,1,82,
        1,82,1,82,1,82,1,82,1,82,5,82,606,8,82,10,82,12,82,609,9,82,1,82,
        1,82,1,82,3,82,614,8,82,1,83,1,83,3,83,618,8,83,1,84,3,84,621,8,
        84,1,85,3,85,624,8,85,1,86,3,86,627,8,86,1,87,1,87,1,87,1,88,4,88,
        633,8,88,11,88,12,88,634,1,89,1,89,5,89,639,8,89,10,89,12,89,642,
        9,89,1,90,1,90,3,90,646,8,90,1,90,3,90,649,8,90,1,90,1,90,3,90,653,
        8,90,1,91,1,91,1,92,1,92,1,93,1,93,3,93,661,8,93,1,94,1,94,1,94,
        3,94,666,8,94,4,489,502,594,607,0,95,1,3,3,4,5,5,7,6,9,7,11,8,13,
        9,15,10,17,11,19,12,21,13,23,14,25,15,27,16,29,17,31,18,33,19,35,
        20,37,21,39,22,41,23,43,24,45,25,47,26,49,27,51,28,53,29,55,30,57,
        31,59,32,61,33,63,34,65,35,67,36,69,37,71,38,73,39,75,40,77,41,79,
        42,81,43,83,44,85,45,87,46,89,47,91,48,93,49,95,50,97,51,99,52,101,
        53,103,54,105,55,107,56,109,57,111,58,113,59,115,60,117,61,119,62,
        121,63,123,64,125,65,127,66,129,67,131,68,133,0,135,0,137,0,139,
        0,141,0,143,0,145,0,147,0,149,0,151,0,153,0,155,0,157,0,159,0,161,
        0,163,0,165,0,167,0,169,0,171,0,173,0,175,0,177,0,179,0,181,0,183,
        0,185,0,187,0,189,0,1,0,27,6,0,70,70,82,82,85,85,102,102,114,114,
        117,117,2,0,70,70,102,102,2,0,82,82,114,114,2,0,66,66,98,98,2,0,
        79,79,111,111,2,0,88,88,120,120,2,0,74,74,106,106,4,0,10,10,12,13,
        39,39,92,92,4,0,10,10,12,13,34,34,92,92,1,0,92,92,1,0,49,57,1,0,
        48,57,1,0,48,55,3,0,48,57,65,70,97,102,1,0,48,49,2,0,69,69,101,101,
        2,0,43,43,45,45,5,0,0,9,11,12,14,38,40,91,93,127,5,0,0,9,11,12,14,
        33,35,91,93,127,2,0,0,91,93,127,1,0,0,127,2,0,9,9,32,32,2,0,10,10,
        12,13,4,0,6277,6278,8472,8472,8494,8494,12443,12444,4,0,183,183,
        903,903,4969,4977,6618,6618,652,0,65,90,95,95,97,122,170,170,181,
        181,186,186,192,214,216,246,248,705,710,721,736,740,748,748,750,
        750,880,884,886,887,890,893,895,895,902,902,904,906,908,908,910,
        929,931,1013,1015,1153,1162,1327,1329,1366,1369,1369,1376,1416,1488,
        1514,1519,1522,1568,1610,1646,1647,1649,1747,1749,1749,1765,1766,
        1774,1775,1786,1788,1791,1791,1808,1808,1810,1839,1869,1957,1969,
        1969,1994,2026,2036,2037,2042,2042,2048,2069,2074,2074,2084,2084,
        2088,2088,2112,2136,2144,2154,2160,2183,2185,2190,2208,2249,2308,
        2361,2365,2365,2384,2384,2392,2401,2417,2432,2437,2444,2447,2448,
        2451,2472,2474,2480,2482,2482,2486,2489,2493,2493,2510,2510,2524,
        2525,2527,2529,2544,2545,2556,2556,2565,2570,2575,2576,2579,2600,
        2602,2608,2610,2611,2613,2614,2616,2617,2649,2652,2654,2654,2674,
        2676,2693,2701,2703,2705,2707,2728,2730,2736,2738,2739,2741,2745,
        2749,2749,2768,2768,2784,2785,2809,2809,2821,2828,2831,2832,2835,
        2856,2858,2864,2866,2867,2869,2873,2877,2877,2908,2909,2911,2913,
        2929,2929,2947,2947,2949,2954,2958,2960,2962,2965,2969,2970,2972,
        2972,2974,2975,2979,2980,2984,2986,2990,3001,3024,3024,3077,3084,
        3086,3088,3090,3112,3114,3129,3133,3133,3160,3162,3165,3165,3168,
        3169,3200,3200,3205,3212,3214,3216,3218,3240,3242,3251,3253,3257,
        3261,3261,3293,3294,3296,3297,3313,3314,3332,3340,3342,3344,3346,
        3386,3389,3389,3406,3406,3412,3414,3423,3425,3450,3455,3461,3478,
        3482,3505,3507,3515,3517,3517,3520,3526,3585,3632,3634,3635,3648,
        3654,3713,3714,3716,3716,3718,3722,3724,3747,3749,3749,3751,3760,
        3762,3763,3773,3773,3776,3780,3782,3782,3804,3807,3840,3840,3904,
        3911,3913,3948,3976,3980,4096,4138,4159,4159,4176,4181,4186,4189,
        4193,4193,4197,4198,4206,4208,4213,4225,4238,4238,4256,4293,4295,
        4295,4301,4301,4304,4346,4348,4680,4682,4685,4688,4694,4696,4696,
        4698,4701,4704,4744,4746,4749,4752,4784,4786,4789,4792,4798,4800,
        4800,4802,4805,4808,4822,4824,4880,4882,4885,4888,4954,4992,5007,
        5024,5109,5112,5117,5121,5740,5743,5759,5761,5786,5792,5866,5870,
        5880,5888,5905,5919,5937,5952,5969,5984,5996,5998,6000,6016,6067,
        6103,6103,6108,6108,6176,6264,6272,6276,6279,6312,6314,6314,6320,
        6389,6400,6430,6480,6509,6512,6516,6528,6571,6576,6601,6656,6678,
        6688,6740,6823,6823,6917,6963,6981,6988,7043,7072,7086,7087,7098,
        7141,7168,7203,7245,7247,7258,7293,7296,7304,7312,7354,7357,7359,
        7401,7404,7406,7411,7413,7414,7418,7418,7424,7615,7680,7957,7960,
        7965,7968,8005,8008,8013,8016,8023,8025,8025,8027,8027,8029,8029,
        8031,8061,8064,8116,8118,8124,8126,8126,8130,8132,8134,8140,8144,
        8147,8150,8155,8160,8172,8178,8180,8182,8188,8305,8305,8319,8319,
        8336,8348,8450,8450,8455,8455,8458,8467,8469,8469,8473,8477,8484,
        8484,8486,8486,8488,8488,8490,8493,8495,8505,8508,8511,8517,8521,
        8526,8526,8544,8584,11264,11492,11499,11502,11506,11507,11520,11557,
        11559,11559,11565,11565,11568,11623,11631,11631,11648,11670,11680,
        11686,11688,11694,11696,11702,11704,11710,11712,11718,11720,11726,
        11728,11734,11736,11742,11823,11823,12293,12295,12321,12329,12337,
        12341,12344,12348,12353,12438,12445,12447,12449,12538,12540,12543,
        12549,12591,12593,12686,12704,12735,12784,12799,13312,19903,19968,
        42124,42192,42237,42240,42508,42512,42527,42538,42539,42560,42606,
        42623,42653,42656,42735,42775,42783,42786,42888,42891,42954,42960,
        42961,42963,42963,42965,42969,42994,43009,43011,43013,43015,43018,
        43020,43042,43072,43123,43138,43187,43250,43255,43259,43259,43261,
        43262,43274,43301,43312,43334,43360,43388,43396,43442,43471,43471,
        43488,43492,43494,43503,43514,43518,43520,43560,43584,43586,43588,
        43595,43616,43638,43642,43642,43646,43695,43697,43697,43701,43702,
        43705,43709,43712,43712,43714,43714,43739,43741,43744,43754,43762,
        43764,43777,43782,43785,43790,43793,43798,43808,43814,43816,43822,
        43824,43866,43868,43881,43888,44002,44032,55203,55216,55238,55243,
        55291,63744,64109,64112,64217,64256,64262,64275,64279,64285,64285,
        64287,64296,64298,64310,64312,64316,64318,64318,64320,64321,64323,
        64324,64326,64433,64467,64829,64848,64911,64914,64967,65008,65019,
        65136,65140,65142,65276,65313,65338,65345,65370,65382,65470,65474,
        65479,65482,65487,65490,65495,65498,65500,65536,65547,65549,65574,
        65576,65594,65596,65597,65599,65613,65616,65629,65664,65786,65856,
        65908,66176,66204,66208,66256,66304,66335,66349,66378,66384,66421,
        66432,66461,66464,66499,66504,66511,66513,66517,66560,66717,66736,
        66771,66776,66811,66816,66855,66864,66915,66928,66938,66940,66954,
        66956,66962,66964,66965,66967,66977,66979,66993,66995,67001,67003,
        67004,67072,67382,67392,67413,67424,67431,67456,67461,67463,67504,
        67506,67514,67584,67589,67592,67592,67594,67637,67639,67640,67644,
        67644,67647,67669,67680,67702,67712,67742,67808,67826,67828,67829,
        67840,67861,67872,67897,67968,68023,68030,68031,68096,68096,68112,
        68115,68117,68119,68121,68149,68192,68220,68224,68252,68288,68295,
        68297,68324,68352,68405,68416,68437,68448,68466,68480,68497,68608,
        68680,68736,68786,68800,68850,68864,68899,69248,69289,69296,69297,
        69376,69404,69415,69415,69424,69445,69488,69505,69552,69572,69600,
        69622,69635,69687,69745,69746,69749,69749,69763,69807,69840,69864,
        69891,69926,69956,69956,69959,69959,69968,70002,70006,70006,70019,
        70066,70081,70084,70106,70106,70108,70108,70144,70161,70163,70187,
        70272,70278,70280,70280,70282,70285,70287,70301,70303,70312,70320,
        70366,70405,70412,70415,70416,70419,70440,70442,70448,70450,70451,
        70453,70457,70461,70461,70480,70480,70493,70497,70656,70708,70727,
        70730,70751,70753,70784,70831,70852,70853,70855,70855,71040,71086,
        71128,71131,71168,71215,71236,71236,71296,71338,71352,71352,71424,
        71450,71488,71494,71680,71723,71840,71903,71935,71942,71945,71945,
        71948,71955,71957,71958,71960,71983,71999,71999,72001,72001,72096,
        72103,72106,72144,72161,72161,72163,72163,72192,72192,72203,72242,
        72250,72250,72272,72272,72284,72329,72349,72349,72368,72440,72704,
        72712,72714,72750,72768,72768,72818,72847,72960,72966,72968,72969,
        72971,73008,73030,73030,73056,73061,73063,73064,73066,73097,73112,
        73112,73440,73458,73648,73648,73728,74649,74752,74862,74880,75075,
        77712,77808,77824,78894,82944,83526,92160,92728,92736,92766,92784,
        92862,92880,92909,92928,92975,92992,92995,93027,93047,93053,93071,
        93760,93823,93952,94026,94032,94032,94099,94111,94176,94177,94179,
        94179,94208,100343,100352,101589,101632,101640,110576,110579,110581,
        110587,110589,110590,110592,110882,110928,110930,110948,110951,110960,
        111355,113664,113770,113776,113788,113792,113800,113808,113817,119808,
        119892,119894,119964,119966,119967,119970,119970,119973,119974,119977,
        119980,119982,119993,119995,119995,119997,120003,120005,120069,120071,
        120074,120077,120084,120086,120092,120094,120121,120123,120126,120128,
        120132,120134,120134,120138,120144,120146,120485,120488,120512,120514,
        120538,120540,120570,120572,120596,120598,120628,120630,120654,120656,
        120686,120688,120712,120714,120744,120746,120770,120772,120779,122624,
        122654,123136,123180,123191,123197,123214,123214,123536,123565,123584,
        123627,124896,124902,124904,124907,124909,124910,124912,124926,124928,
        125124,125184,125251,125259,125259,126464,126467,126469,126495,126497,
        126498,126500,126500,126503,126503,126505,126514,126516,126519,126521,
        126521,126523,126523,126530,126530,126535,126535,126537,126537,126539,
        126539,126541,126543,126545,126546,126548,126548,126551,126551,126553,
        126553,126555,126555,126557,126557,126559,126559,126561,126562,126564,
        126564,126567,126570,126572,126578,126580,126583,126585,126588,126590,
        126590,126592,126601,126603,126619,126625,126627,126629,126633,126635,
        126651,131072,173791,173824,177976,177984,178205,178208,183969,183984,
        191456,194560,195101,196608,201546,360,0,48,57,95,95,768,879,1155,
        1159,1425,1469,1471,1471,1473,1474,1476,1477,1479,1479,1552,1562,
        1611,1641,1648,1648,1750,1756,1759,1764,1767,1768,1770,1773,1776,
        1785,1809,1809,1840,1866,1958,1968,1984,1993,2027,2035,2045,2045,
        2070,2073,2075,2083,2085,2087,2089,2093,2137,2139,2200,2207,2250,
        2273,2275,2307,2362,2364,2366,2383,2385,2391,2402,2403,2406,2415,
        2433,2435,2492,2492,2494,2500,2503,2504,2507,2509,2519,2519,2530,
        2531,2534,2543,2558,2558,2561,2563,2620,2620,2622,2626,2631,2632,
        2635,2637,2641,2641,2662,2673,2677,2677,2689,2691,2748,2748,2750,
        2757,2759,2761,2763,2765,2786,2787,2790,2799,2810,2815,2817,2819,
        2876,2876,2878,2884,2887,2888,2891,2893,2901,2903,2914,2915,2918,
        2927,2946,2946,3006,3010,3014,3016,3018,3021,3031,3031,3046,3055,
        3072,3076,3132,3132,3134,3140,3142,3144,3146,3149,3157,3158,3170,
        3171,3174,3183,3201,3203,3260,3260,3262,3268,3270,3272,3274,3277,
        3285,3286,3298,3299,3302,3311,3328,3331,3387,3388,3390,3396,3398,
        3400,3402,3405,3415,3415,3426,3427,3430,3439,3457,3459,3530,3530,
        3535,3540,3542,3542,3544,3551,3558,3567,3570,3571,3633,3633,3636,
        3642,3655,3662,3664,3673,3761,3761,3764,3772,3784,3789,3792,3801,
        3864,3865,3872,3881,3893,3893,3895,3895,3897,3897,3902,3903,3953,
        3972,3974,3975,3981,3991,3993,4028,4038,4038,4139,4158,4160,4169,
        4182,4185,4190,4192,4194,4196,4199,4205,4209,4212,4226,4237,4239,
        4253,4957,4959,5906,5909,5938,5940,5970,5971,6002,6003,6068,6099,
        6109,6109,6112,6121,6155,6157,6159,6169,6277,6278,6313,6313,6432,
        6443,6448,6459,6470,6479,6608,6617,6679,6683,6741,6750,6752,6780,
        6783,6793,6800,6809,6832,6845,6847,6862,6912,6916,6964,6980,6992,
        7001,7019,7027,7040,7042,7073,7085,7088,7097,7142,7155,7204,7223,
        7232,7241,7248,7257,7376,7378,7380,7400,7405,7405,7412,7412,7415,
        7417,7616,7679,8255,8256,8276,8276,8400,8412,8417,8417,8421,8432,
        11503,11505,11647,11647,11744,11775,12330,12335,12441,12442,42528,
        42537,42607,42607,42612,42621,42654,42655,42736,42737,43010,43010,
        43014,43014,43019,43019,43043,43047,43052,43052,43136,43137,43188,
        43205,43216,43225,43232,43249,43263,43273,43302,43309,43335,43347,
        43392,43395,43443,43456,43472,43481,43493,43493,43504,43513,43561,
        43574,43587,43587,43596,43597,43600,43609,43643,43645,43696,43696,
        43698,43700,43703,43704,43710,43711,43713,43713,43755,43759,43765,
        43766,44003,44010,44012,44013,44016,44025,64286,64286,65024,65039,
        65056,65071,65075,65076,65101,65103,65296,65305,65343,65343,66045,
        66045,66272,66272,66422,66426,66720,66729,68097,68099,68101,68102,
        68108,68111,68152,68154,68159,68159,68325,68326,68900,68903,68912,
        68921,69291,69292,69446,69456,69506,69509,69632,69634,69688,69702,
        69734,69744,69747,69748,69759,69762,69808,69818,69826,69826,69872,
        69881,69888,69890,69927,69940,69942,69951,69957,69958,70003,70003,
        70016,70018,70067,70080,70089,70092,70094,70105,70188,70199,70206,
        70206,70367,70378,70384,70393,70400,70403,70459,70460,70462,70468,
        70471,70472,70475,70477,70487,70487,70498,70499,70502,70508,70512,
        70516,70709,70726,70736,70745,70750,70750,70832,70851,70864,70873,
        71087,71093,71096,71104,71132,71133,71216,71232,71248,71257,71339,
        71351,71360,71369,71453,71467,71472,71481,71724,71738,71904,71913,
        71984,71989,71991,71992,71995,71998,72000,72000,72002,72003,72016,
        72025,72145,72151,72154,72160,72164,72164,72193,72202,72243,72249,
        72251,72254,72263,72263,72273,72283,72330,72345,72751,72758,72760,
        72767,72784,72793,72850,72871,72873,72886,73009,73014,73018,73018,
        73020,73021,73023,73029,73031,73031,73040,73049,73098,73102,73104,
        73105,73107,73111,73120,73129,73459,73462,92768,92777,92864,92873,
        92912,92916,92976,92982,93008,93017,94031,94031,94033,94087,94095,
        94098,94180,94180,94192,94193,113821,113822,118528,118573,118576,
        118598,119141,119145,119149,119154,119163,119170,119173,119179,119210,
        119213,119362,119364,120782,120831,121344,121398,121403,121452,121461,
        121461,121476,121476,121499,121503,121505,121519,122880,122886,122888,
        122904,122907,122913,122915,122916,122918,122922,123184,123190,123200,
        123209,123566,123566,123628,123641,125136,125142,125252,125258,125264,
        125273,130032,130041,917760,917999,699,0,1,1,0,0,0,0,3,1,0,0,0,0,
        5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,
        1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,
        1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,
        1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,
        1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,
        1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,
        1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,
        1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,
        1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,
        1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,
        105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,
        0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,
        1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,
        1,193,1,0,0,0,3,198,1,0,0,0,5,204,1,0,0,0,7,206,1,0,0,0,9,216,1,
        0,0,0,11,223,1,0,0,0,13,227,1,0,0,0,15,246,1,0,0,0,17,250,1,0,0,
        0,19,262,1,0,0,0,21,273,1,0,0,0,23,291,1,0,0,0,25,293,1,0,0,0,27,
        300,1,0,0,0,29,307,1,0,0,0,31,316,1,0,0,0,33,320,1,0,0,0,35,324,
        1,0,0,0,37,326,1,0,0,0,39,330,1,0,0,0,41,332,1,0,0,0,43,335,1,0,
        0,0,45,338,1,0,0,0,47,340,1,0,0,0,49,342,1,0,0,0,51,344,1,0,0,0,
        53,347,1,0,0,0,55,349,1,0,0,0,57,352,1,0,0,0,59,355,1,0,0,0,61,357,
        1,0,0,0,63,359,1,0,0,0,65,361,1,0,0,0,67,364,1,0,0,0,69,367,1,0,
        0,0,71,369,1,0,0,0,73,371,1,0,0,0,75,373,1,0,0,0,77,375,1,0,0,0,
        79,378,1,0,0,0,81,380,1,0,0,0,83,383,1,0,0,0,85,386,1,0,0,0,87,388,
        1,0,0,0,89,390,1,0,0,0,91,393,1,0,0,0,93,396,1,0,0,0,95,399,1,0,
        0,0,97,402,1,0,0,0,99,405,1,0,0,0,101,407,1,0,0,0,103,410,1,0,0,
        0,105,413,1,0,0,0,107,416,1,0,0,0,109,419,1,0,0,0,111,422,1,0,0,
        0,113,425,1,0,0,0,115,428,1,0,0,0,117,431,1,0,0,0,119,434,1,0,0,
        0,121,437,1,0,0,0,123,441,1,0,0,0,125,445,1,0,0,0,127,449,1,0,0,
        0,129,456,1,0,0,0,131,460,1,0,0,0,133,480,1,0,0,0,135,508,1,0,0,
        0,137,512,1,0,0,0,139,514,1,0,0,0,141,520,1,0,0,0,143,522,1,0,0,
        0,145,524,1,0,0,0,147,526,1,0,0,0,149,528,1,0,0,0,151,530,1,0,0,
        0,153,539,1,0,0,0,155,543,1,0,0,0,157,548,1,0,0,0,159,552,1,0,0,
        0,161,558,1,0,0,0,163,585,1,0,0,0,165,613,1,0,0,0,167,617,1,0,0,
        0,169,620,1,0,0,0,171,623,1,0,0,0,173,626,1,0,0,0,175,628,1,0,0,
        0,177,632,1,0,0,0,179,636,1,0,0,0,181,643,1,0,0,0,183,654,1,0,0,
        0,185,656,1,0,0,0,187,660,1,0,0,0,189,665,1,0,0,0,191,194,3,19,9,
        0,192,194,3,21,10,0,193,191,1,0,0,0,193,192,1,0,0,0,194,2,1,0,0,
        0,195,199,3,5,2,0,196,199,3,31,15,0,197,199,3,33,16,0,198,195,1,
        0,0,0,198,196,1,0,0,0,198,197,1,0,0,0,199,4,1,0,0,0,200,205,3,23,
        11,0,201,205,3,25,12,0,202,205,3,27,13,0,203,205,3,29,14,0,204,200,
        1,0,0,0,204,201,1,0,0,0,204,202,1,0,0,0,204,203,1,0,0,0,205,6,1,
        0,0,0,206,207,5,99,0,0,207,208,5,111,0,0,208,209,5,109,0,0,209,210,
        5,112,0,0,210,211,5,111,0,0,211,212,5,110,0,0,212,213,5,101,0,0,
        213,214,5,110,0,0,214,215,5,116,0,0,215,8,1,0,0,0,216,217,5,109,
        0,0,217,218,5,111,0,0,218,219,5,100,0,0,219,220,5,117,0,0,220,221,
        5,108,0,0,221,222,5,101,0,0,222,10,1,0,0,0,223,224,5,112,0,0,224,
        225,5,105,0,0,225,226,5,110,0,0,226,12,1,0,0,0,227,228,5,115,0,0,
        228,229,5,105,0,0,229,230,5,103,0,0,230,231,5,110,0,0,231,232,5,
        97,0,0,232,233,5,108,0,0,233,14,1,0,0,0,234,235,4,7,0,0,235,247,
        3,177,88,0,236,238,5,13,0,0,237,236,1,0,0,0,237,238,1,0,0,0,238,
        239,1,0,0,0,239,242,5,10,0,0,240,242,2,12,13,0,241,237,1,0,0,0,241,
        240,1,0,0,0,242,244,1,0,0,0,243,245,3,177,88,0,244,243,1,0,0,0,244,
        245,1,0,0,0,245,247,1,0,0,0,246,234,1,0,0,0,246,241,1,0,0,0,247,
        248,1,0,0,0,248,249,6,7,0,0,249,16,1,0,0,0,250,254,3,187,93,0,251,
        253,3,189,94,0,252,251,1,0,0,0,253,256,1,0,0,0,254,252,1,0,0,0,254,
        255,1,0,0,0,255,18,1,0,0,0,256,254,1,0,0,0,257,263,7,0,0,0,258,259,
        7,1,0,0,259,263,7,2,0,0,260,261,7,2,0,0,261,263,7,1,0,0,262,257,
        1,0,0,0,262,258,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,266,
        1,0,0,0,264,267,3,133,66,0,265,267,3,135,67,0,266,264,1,0,0,0,266,
        265,1,0,0,0,267,20,1,0,0,0,268,274,7,3,0,0,269,270,7,3,0,0,270,274,
        7,2,0,0,271,272,7,2,0,0,272,274,7,3,0,0,273,268,1,0,0,0,273,269,
        1,0,0,0,273,271,1,0,0,0,274,277,1,0,0,0,275,278,3,163,81,0,276,278,
        3,165,82,0,277,275,1,0,0,0,277,276,1,0,0,0,278,22,1,0,0,0,279,283,
        3,143,71,0,280,282,3,145,72,0,281,280,1,0,0,0,282,285,1,0,0,0,283,
        281,1,0,0,0,283,284,1,0,0,0,284,292,1,0,0,0,285,283,1,0,0,0,286,
        288,5,48,0,0,287,286,1,0,0,0,288,289,1,0,0,0,289,287,1,0,0,0,289,
        290,1,0,0,0,290,292,1,0,0,0,291,279,1,0,0,0,291,287,1,0,0,0,292,
        24,1,0,0,0,293,294,5,48,0,0,294,296,7,4,0,0,295,297,3,147,73,0,296,
        295,1,0,0,0,297,298,1,0,0,0,298,296,1,0,0,0,298,299,1,0,0,0,299,
        26,1,0,0,0,300,301,5,48,0,0,301,303,7,5,0,0,302,304,3,149,74,0,303,
        302,1,0,0,0,304,305,1,0,0,0,305,303,1,0,0,0,305,306,1,0,0,0,306,
        28,1,0,0,0,307,308,5,48,0,0,308,310,7,3,0,0,309,311,3,151,75,0,310,
        309,1,0,0,0,311,312,1,0,0,0,312,310,1,0,0,0,312,313,1,0,0,0,313,
        30,1,0,0,0,314,317,3,153,76,0,315,317,3,155,77,0,316,314,1,0,0,0,
        316,315,1,0,0,0,317,32,1,0,0,0,318,321,3,31,15,0,319,321,3,157,78,
        0,320,318,1,0,0,0,320,319,1,0,0,0,321,322,1,0,0,0,322,323,7,6,0,
        0,323,34,1,0,0,0,324,325,5,46,0,0,325,36,1,0,0,0,326,327,5,46,0,
        0,327,328,5,46,0,0,328,329,5,46,0,0,329,38,1,0,0,0,330,331,5,42,
        0,0,331,40,1,0,0,0,332,333,5,40,0,0,333,334,6,20,1,0,334,42,1,0,
        0,0,335,336,5,41,0,0,336,337,6,21,2,0,337,44,1,0,0,0,338,339,5,44,
        0,0,339,46,1,0,0,0,340,341,5,58,0,0,341,48,1,0,0,0,342,343,5,59,
        0,0,343,50,1,0,0,0,344,345,5,42,0,0,345,346,5,42,0,0,346,52,1,0,
        0,0,347,348,5,61,0,0,348,54,1,0,0,0,349,350,5,91,0,0,350,351,6,27,
        3,0,351,56,1,0,0,0,352,353,5,93,0,0,353,354,6,28,4,0,354,58,1,0,
        0,0,355,356,5,124,0,0,356,60,1,0,0,0,357,358,5,94,0,0,358,62,1,0,
        0,0,359,360,5,38,0,0,360,64,1,0,0,0,361,362,5,60,0,0,362,363,5,60,
        0,0,363,66,1,0,0,0,364,365,5,62,0,0,365,366,5,62,0,0,366,68,1,0,
        0,0,367,368,5,43,0,0,368,70,1,0,0,0,369,370,5,45,0,0,370,72,1,0,
        0,0,371,372,5,47,0,0,372,74,1,0,0,0,373,374,5,37,0,0,374,76,1,0,
        0,0,375,376,5,47,0,0,376,377,5,47,0,0,377,78,1,0,0,0,378,379,5,126,
        0,0,379,80,1,0,0,0,380,381,5,123,0,0,381,382,6,40,5,0,382,82,1,0,
        0,0,383,384,5,125,0,0,384,385,6,41,6,0,385,84,1,0,0,0,386,387,5,
        60,0,0,387,86,1,0,0,0,388,389,5,62,0,0,389,88,1,0,0,0,390,391,5,
        61,0,0,391,392,5,61,0,0,392,90,1,0,0,0,393,394,5,62,0,0,394,395,
        5,61,0,0,395,92,1,0,0,0,396,397,5,60,0,0,397,398,5,61,0,0,398,94,
        1,0,0,0,399,400,5,60,0,0,400,401,5,62,0,0,401,96,1,0,0,0,402,403,
        5,33,0,0,403,404,5,61,0,0,404,98,1,0,0,0,405,406,5,64,0,0,406,100,
        1,0,0,0,407,408,5,45,0,0,408,409,5,62,0,0,409,102,1,0,0,0,410,411,
        5,43,0,0,411,412,5,61,0,0,412,104,1,0,0,0,413,414,5,45,0,0,414,415,
        5,61,0,0,415,106,1,0,0,0,416,417,5,42,0,0,417,418,5,61,0,0,418,108,
        1,0,0,0,419,420,5,64,0,0,420,421,5,61,0,0,421,110,1,0,0,0,422,423,
        5,47,0,0,423,424,5,61,0,0,424,112,1,0,0,0,425,426,5,37,0,0,426,427,
        5,61,0,0,427,114,1,0,0,0,428,429,5,38,0,0,429,430,5,61,0,0,430,116,
        1,0,0,0,431,432,5,124,0,0,432,433,5,61,0,0,433,118,1,0,0,0,434,435,
        5,94,0,0,435,436,5,61,0,0,436,120,1,0,0,0,437,438,5,60,0,0,438,439,
        5,60,0,0,439,440,5,61,0,0,440,122,1,0,0,0,441,442,5,62,0,0,442,443,
        5,62,0,0,443,444,5,61,0,0,444,124,1,0,0,0,445,446,5,42,0,0,446,447,
        5,42,0,0,447,448,5,61,0,0,448,126,1,0,0,0,449,450,5,47,0,0,450,451,
        5,47,0,0,451,452,5,61,0,0,452,128,1,0,0,0,453,457,3,177,88,0,454,
        457,3,179,89,0,455,457,3,181,90,0,456,453,1,0,0,0,456,454,1,0,0,
        0,456,455,1,0,0,0,457,458,1,0,0,0,458,459,6,64,7,0,459,130,1,0,0,
        0,460,461,9,0,0,0,461,132,1,0,0,0,462,467,5,39,0,0,463,466,3,141,
        70,0,464,466,8,7,0,0,465,463,1,0,0,0,465,464,1,0,0,0,466,469,1,0,
        0,0,467,465,1,0,0,0,467,468,1,0,0,0,468,470,1,0,0,0,469,467,1,0,
        0,0,470,481,5,39,0,0,471,476,5,34,0,0,472,475,3,141,70,0,473,475,
        8,8,0,0,474,472,1,0,0,0,474,473,1,0,0,0,475,478,1,0,0,0,476,474,
        1,0,0,0,476,477,1,0,0,0,477,479,1,0,0,0,478,476,1,0,0,0,479,481,
        5,34,0,0,480,462,1,0,0,0,480,471,1,0,0,0,481,134,1,0,0,0,482,483,
        5,39,0,0,483,484,5,39,0,0,484,485,5,39,0,0,485,489,1,0,0,0,486,488,
        3,137,68,0,487,486,1,0,0,0,488,491,1,0,0,0,489,490,1,0,0,0,489,487,
        1,0,0,0,490,492,1,0,0,0,491,489,1,0,0,0,492,493,5,39,0,0,493,494,
        5,39,0,0,494,509,5,39,0,0,495,496,5,34,0,0,496,497,5,34,0,0,497,
        498,5,34,0,0,498,502,1,0,0,0,499,501,3,137,68,0,500,499,1,0,0,0,
        501,504,1,0,0,0,502,503,1,0,0,0,502,500,1,0,0,0,503,505,1,0,0,0,
        504,502,1,0,0,0,505,506,5,34,0,0,506,507,5,34,0,0,507,509,5,34,0,
        0,508,482,1,0,0,0,508,495,1,0,0,0,509,136,1,0,0,0,510,513,3,139,
        69,0,511,513,3,141,70,0,512,510,1,0,0,0,512,511,1,0,0,0,513,138,
        1,0,0,0,514,515,8,9,0,0,515,140,1,0,0,0,516,517,5,92,0,0,517,521,
        9,0,0,0,518,519,5,92,0,0,519,521,3,15,7,0,520,516,1,0,0,0,520,518,
        1,0,0,0,521,142,1,0,0,0,522,523,7,10,0,0,523,144,1,0,0,0,524,525,
        7,11,0,0,525,146,1,0,0,0,526,527,7,12,0,0,527,148,1,0,0,0,528,529,
        7,13,0,0,529,150,1,0,0,0,530,531,7,14,0,0,531,152,1,0,0,0,532,534,
        3,157,78,0,533,532,1,0,0,0,533,534,1,0,0,0,534,535,1,0,0,0,535,540,
        3,159,79,0,536,537,3,157,78,0,537,538,5,46,0,0,538,540,1,0,0,0,539,
        533,1,0,0,0,539,536,1,0,0,0,540,154,1,0,0,0,541,544,3,157,78,0,542,
        544,3,153,76,0,543,541,1,0,0,0,543,542,1,0,0,0,544,545,1,0,0,0,545,
        546,3,161,80,0,546,156,1,0,0,0,547,549,3,145,72,0,548,547,1,0,0,
        0,549,550,1,0,0,0,550,548,1,0,0,0,550,551,1,0,0,0,551,158,1,0,0,
        0,552,554,5,46,0,0,553,555,3,145,72,0,554,553,1,0,0,0,555,556,1,
        0,0,0,556,554,1,0,0,0,556,557,1,0,0,0,557,160,1,0,0,0,558,560,7,
        15,0,0,559,561,7,16,0,0,560,559,1,0,0,0,560,561,1,0,0,0,561,563,
        1,0,0,0,562,564,3,145,72,0,563,562,1,0,0,0,564,565,1,0,0,0,565,563,
        1,0,0,0,565,566,1,0,0,0,566,162,1,0,0,0,567,572,5,39,0,0,568,571,
        3,169,84,0,569,571,3,175,87,0,570,568,1,0,0,0,570,569,1,0,0,0,571,
        574,1,0,0,0,572,570,1,0,0,0,572,573,1,0,0,0,573,575,1,0,0,0,574,
        572,1,0,0,0,575,586,5,39,0,0,576,581,5,34,0,0,577,580,3,171,85,0,
        578,580,3,175,87,0,579,577,1,0,0,0,579,578,1,0,0,0,580,583,1,0,0,
        0,581,579,1,0,0,0,581,582,1,0,0,0,582,584,1,0,0,0,583,581,1,0,0,
        0,584,586,5,34,0,0,585,567,1,0,0,0,585,576,1,0,0,0,586,164,1,0,0,
        0,587,588,5,39,0,0,588,589,5,39,0,0,589,590,5,39,0,0,590,594,1,0,
        0,0,591,593,3,167,83,0,592,591,1,0,0,0,593,596,1,0,0,0,594,595,1,
        0,0,0,594,592,1,0,0,0,595,597,1,0,0,0,596,594,1,0,0,0,597,598,5,
        39,0,0,598,599,5,39,0,0,599,614,5,39,0,0,600,601,5,34,0,0,601,602,
        5,34,0,0,602,603,5,34,0,0,603,607,1,0,0,0,604,606,3,167,83,0,605,
        604,1,0,0,0,606,609,1,0,0,0,607,608,1,0,0,0,607,605,1,0,0,0,608,
        610,1,0,0,0,609,607,1,0,0,0,610,611,5,34,0,0,611,612,5,34,0,0,612,
        614,5,34,0,0,613,587,1,0,0,0,613,600,1,0,0,0,614,166,1,0,0,0,615,
        618,3,173,86,0,616,618,3,175,87,0,617,615,1,0,0,0,617,616,1,0,0,
        0,618,168,1,0,0,0,619,621,7,17,0,0,620,619,1,0,0,0,621,170,1,0,0,
        0,622,624,7,18,0,0,623,622,1,0,0,0,624,172,1,0,0,0,625,627,7,19,
        0,0,626,625,1,0,0,0,627,174,1,0,0,0,628,629,5,92,0,0,629,630,7,20,
        0,0,630,176,1,0,0,0,631,633,7,21,0,0,632,631,1,0,0,0,633,634,1,0,
        0,0,634,632,1,0,0,0,634,635,1,0,0,0,635,178,1,0,0,0,636,640,5,35,
        0,0,637,639,8,22,0,0,638,637,1,0,0,0,639,642,1,0,0,0,640,638,1,0,
        0,0,640,641,1,0,0,0,641,180,1,0,0,0,642,640,1,0,0,0,643,645,5,92,
        0,0,644,646,3,177,88,0,645,644,1,0,0,0,645,646,1,0,0,0,646,652,1,
        0,0,0,647,649,5,13,0,0,648,647,1,0,0,0,648,649,1,0,0,0,649,650,1,
        0,0,0,650,653,5,10,0,0,651,653,2,12,13,0,652,648,1,0,0,0,652,651,
        1,0,0,0,653,182,1,0,0,0,654,655,7,23,0,0,655,184,1,0,0,0,656,657,
        7,24,0,0,657,186,1,0,0,0,658,661,7,25,0,0,659,661,3,183,91,0,660,
        658,1,0,0,0,660,659,1,0,0,0,661,188,1,0,0,0,662,666,3,187,93,0,663,
        666,7,26,0,0,664,666,3,185,92,0,665,662,1,0,0,0,665,663,1,0,0,0,
        665,664,1,0,0,0,666,190,1,0,0,0,58,0,193,198,204,237,241,244,246,
        254,262,266,273,277,283,289,291,298,305,312,316,320,456,465,467,
        474,476,480,489,502,508,512,520,533,539,543,550,556,560,565,570,
        572,579,581,585,594,607,613,617,620,623,626,634,640,645,648,652,
        660,665,8,1,7,0,1,20,1,1,21,2,1,27,3,1,28,4,1,40,5,1,41,6,6,0,0
    ]

class AtopileLexer(AtopileLexerBase):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INDENT = 1
    DEDENT = 2
    STRING = 3
    NUMBER = 4
    INTEGER = 5
    COMPONENT = 6
    MODULE = 7
    PIN = 8
    SIGNAL = 9
    NEWLINE = 10
    NAME = 11
    STRING_LITERAL = 12
    BYTES_LITERAL = 13
    DECIMAL_INTEGER = 14
    OCT_INTEGER = 15
    HEX_INTEGER = 16
    BIN_INTEGER = 17
    FLOAT_NUMBER = 18
    IMAG_NUMBER = 19
    DOT = 20
    ELLIPSIS = 21
    STAR = 22
    OPEN_PAREN = 23
    CLOSE_PAREN = 24
    COMMA = 25
    COLON = 26
    SEMI_COLON = 27
    POWER = 28
    ASSIGN = 29
    OPEN_BRACK = 30
    CLOSE_BRACK = 31
    OR_OP = 32
    XOR = 33
    AND_OP = 34
    LEFT_SHIFT = 35
    RIGHT_SHIFT = 36
    ADD = 37
    MINUS = 38
    DIV = 39
    MOD = 40
    IDIV = 41
    NOT_OP = 42
    OPEN_BRACE = 43
    CLOSE_BRACE = 44
    LESS_THAN = 45
    GREATER_THAN = 46
    EQUALS = 47
    GT_EQ = 48
    LT_EQ = 49
    NOT_EQ_1 = 50
    NOT_EQ_2 = 51
    AT = 52
    ARROW = 53
    ADD_ASSIGN = 54
    SUB_ASSIGN = 55
    MULT_ASSIGN = 56
    AT_ASSIGN = 57
    DIV_ASSIGN = 58
    MOD_ASSIGN = 59
    AND_ASSIGN = 60
    OR_ASSIGN = 61
    XOR_ASSIGN = 62
    LEFT_SHIFT_ASSIGN = 63
    RIGHT_SHIFT_ASSIGN = 64
    POWER_ASSIGN = 65
    IDIV_ASSIGN = 66
    SKIP_ = 67
    UNKNOWN_CHAR = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'component'", "'module'", "'pin'", "'signal'", "'.'", "'...'", 
            "'*'", "'('", "')'", "','", "':'", "';'", "'**'", "'='", "'['", 
            "']'", "'|'", "'^'", "'&'", "'<<'", "'>>'", "'+'", "'-'", "'/'", 
            "'%'", "'//'", "'~'", "'{'", "'}'", "'<'", "'>'", "'=='", "'>='", 
            "'<='", "'<>'", "'!='", "'@'", "'->'", "'+='", "'-='", "'*='", 
            "'@='", "'/='", "'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='", 
            "'**='", "'//='" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "STRING", "NUMBER", "INTEGER", "COMPONENT", 
            "MODULE", "PIN", "SIGNAL", "NEWLINE", "NAME", "STRING_LITERAL", 
            "BYTES_LITERAL", "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", 
            "BIN_INTEGER", "FLOAT_NUMBER", "IMAG_NUMBER", "DOT", "ELLIPSIS", 
            "STAR", "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", "SEMI_COLON", 
            "POWER", "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", "XOR", 
            "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", "DIV", 
            "MOD", "IDIV", "NOT_OP", "OPEN_BRACE", "CLOSE_BRACE", "LESS_THAN", 
            "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", 
            "AT", "ARROW", "ADD_ASSIGN", "SUB_ASSIGN", "MULT_ASSIGN", "AT_ASSIGN", 
            "DIV_ASSIGN", "MOD_ASSIGN", "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", 
            "LEFT_SHIFT_ASSIGN", "RIGHT_SHIFT_ASSIGN", "POWER_ASSIGN", "IDIV_ASSIGN", 
            "SKIP_", "UNKNOWN_CHAR" ]

    ruleNames = [ "STRING", "NUMBER", "INTEGER", "COMPONENT", "MODULE", 
                  "PIN", "SIGNAL", "NEWLINE", "NAME", "STRING_LITERAL", 
                  "BYTES_LITERAL", "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", 
                  "BIN_INTEGER", "FLOAT_NUMBER", "IMAG_NUMBER", "DOT", "ELLIPSIS", 
                  "STAR", "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", 
                  "SEMI_COLON", "POWER", "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", 
                  "OR_OP", "XOR", "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", 
                  "ADD", "MINUS", "DIV", "MOD", "IDIV", "NOT_OP", "OPEN_BRACE", 
                  "CLOSE_BRACE", "LESS_THAN", "GREATER_THAN", "EQUALS", 
                  "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "AT", "ARROW", 
                  "ADD_ASSIGN", "SUB_ASSIGN", "MULT_ASSIGN", "AT_ASSIGN", 
                  "DIV_ASSIGN", "MOD_ASSIGN", "AND_ASSIGN", "OR_ASSIGN", 
                  "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", "RIGHT_SHIFT_ASSIGN", 
                  "POWER_ASSIGN", "IDIV_ASSIGN", "SKIP_", "UNKNOWN_CHAR", 
                  "SHORT_STRING", "LONG_STRING", "LONG_STRING_ITEM", "LONG_STRING_CHAR", 
                  "STRING_ESCAPE_SEQ", "NON_ZERO_DIGIT", "DIGIT", "OCT_DIGIT", 
                  "HEX_DIGIT", "BIN_DIGIT", "POINT_FLOAT", "EXPONENT_FLOAT", 
                  "INT_PART", "FRACTION", "EXPONENT", "SHORT_BYTES", "LONG_BYTES", 
                  "LONG_BYTES_ITEM", "SHORT_BYTES_CHAR_NO_SINGLE_QUOTE", 
                  "SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE", "LONG_BYTES_CHAR", 
                  "BYTES_ESCAPE_SEQ", "SPACES", "COMMENT", "LINE_JOINING", 
                  "UNICODE_OIDS", "UNICODE_OIDC", "ID_START", "ID_CONTINUE" ]

    grammarFileName = "AtopileLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[7] = self.NEWLINE_action 
            actions[20] = self.OPEN_PAREN_action 
            actions[21] = self.CLOSE_PAREN_action 
            actions[27] = self.OPEN_BRACK_action 
            actions[28] = self.CLOSE_BRACK_action 
            actions[40] = self.OPEN_BRACE_action 
            actions[41] = self.CLOSE_BRACE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.onNewLine();
     

    def OPEN_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.openBrace();
     

    def CLOSE_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.closeBrace();
     

    def OPEN_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.openBrace();
     

    def CLOSE_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.closeBrace();
     

    def OPEN_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.openBrace();
     

    def CLOSE_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.closeBrace();
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[7] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


