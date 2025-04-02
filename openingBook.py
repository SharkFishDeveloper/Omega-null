OPENING_BOOK = {
    # Initial position and common first moves
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1": [
        "e2e4", "d2d4", "c2c4", "g1f3", "f2f4", "b1c3", "g2g3", "b2b3", "e2e3", "a2a3"
    ],

    # Responses to 1.e4
    "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1": [
        "e7e5", "c7c5", "e7e6", "c7c6", "g7g6", "d7d5", "d7d6", "g8f6", "b7b6", "a7a6"
    ],

    # Responses to 1.d4
    "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1": [
        "d7d5", "g8f6", "e7e6", "c7c6", "f7f5", "g7g6", "d7d6", "c7c5", "b7b6", "e7e5"
    ],

    # Responses to 1.c4
    "rnbqkbnr/pppppppp/8/8/2P5/8/PP1PPPPP/RNBQKBNR b KQkq - 0 1": [
        "e7e5", "c7c5", "g8f6", "e7e6", "g7g6", "d7d5", "b7b6", "f7f5", "d7d6", "a7a6"
    ],

    # Responses to 1.Nf3
    "rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R b KQkq - 0 1": [
        "d7d5", "g8f6", "c7c5", "e7e6", "g7g6", "b7b6", "d7d6", "f7f5", "a7a6", "h7h6"
    ],

    # Sicilian Defense (1.e4 c5)
    "rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2": [
        "g1f3", "b1c3", "f2f4", "d2d4", "g2g3", "f1c4", "c2c3", "b2b4", "a2a3", "h2h3"
    ],
    
    # Open Game (1.e4 e5)
    "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2": [
        "g1f3", "f2f4", "f1c4", "b1c3", "d2d4", "g2g3", "d2d3", "h2h3", "c2c3", "a2a3"
    ],
    
    # French Defense (1.e4 e6)
    "rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2": [
        "d2d4", "g1f3", "d2d3", "b1c3", "f2f4", "c2c4", "f1e2", "g2g3", "h2h3", "a2a3"
    ],
    
    # Caro-Kann (1.e4 c6)
    "rnbqkbnr/pp1ppppp/2p5/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2": [
        "d2d4", "g1f3", "b1c3", "f2f4", "c2c4", "d2d3", "f1c4", "g2g3", "h2h3", "a2a3"
    ],
    
    # Pirc/Modern (1.e4 d6)
    "rnbqkbnr/ppp1pppp/3p4/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2": [
        "d2d4", "g1f3", "b1c3", "f2f4", "f1c4", "g2g3", "d2d3", "h2h3", "a2a3", "c2c3"
    ],
    
    # Alekhine's Defense (1.e4 Nf6)
    "rnbqkb1r/pppppppp/5n2/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 1 2": [
        "e4e5", "b1c3", "d2d4", "f1c4", "g1f3", "f2f3", "g2g3", "h2h3", "a2a3", "c2c3"
    ],
    
    # Scandinavian (1.e4 d5)
    "rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2": [
        "e4d5", "d2d4", "b1c3", "g1f3", "f1c4", "g2g3", "h2h3", "a2a3", "c2c3", "f2f3"
    ],
    
    # Queen's Gambit (1.d4 d5 2.c4)
    "rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR b KQkq - 0 2": [
        "e7e6", "c7c6", "c7c5", "g8f6", "d5c4", "e7e5", "b7b6", "a7a6", "h7h6", "f7f5"
    ],
    
    # King's Indian Defense (1.d4 Nf6 2.c4 g6)
    "rnbqkb1r/pppppp1p/5np1/8/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3": [
        "b1c3", "g1f3", "e2e4", "g2g3", "f2f3", "h2h3", "a2a3", "c1g5", "d1b3", "e2e3"
    ],
    
    # Nimzo-Indian Defense (1.d4 Nf6 2.c4 e6 3.Nc3 Bb4)
    "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N5/PP2PPPP/R1BQKBNR w KQkq - 2 4": [
        "d1c2", "g1f3", "a2a3", "e2e3", "f2f3", "g2g3", "c1d2", "d1b3", "h2h3", "e2e4"
    ],
    
    # Grünfeld Defense (1.d4 Nf6 2.c4 g6 3.Nc3 d5)
    "rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq - 0 4": [
        "c4d5", "g1f3", "c1g5", "e2e3", "g2g3", "f2f3", "h2h3", "a2a3", "d1b3", "e2e4"
    ],
    
    # Slav Defense (1.d4 d5 2.c4 c6)
    "rnbqkbnr/pp2pppp/2p5/3p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3": [
        "g1f3", "b1c3", "c4d5", "e2e3", "g2g3", "f2f3", "h2h3", "a2a3", "c1g5", "d1b3"
    ],
    
    # Dutch Defense (1.d4 f5)
    "rnbqkbnr/ppppp1pp/8/5p2/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 2": [
        "g2g3", "g1f3", "c2c4", "e2e4", "f2f3", "h2h3", "a2a3", "c1g5", "d1d3", "b1c3"
    ],
    
    # Benoni Defense (1.d4 Nf6 2.c4 c5)
    "rnbqkb1r/pp1ppppp/5n2/2p5/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3": [
        "d4d5", "g1f3", "b1c3", "e2e3", "g2g3", "f2f3", "h2h3", "a2a3", "c1g5", "d1d2"
    ],
    
    # English Opening (1.c4 e5)
    "rnbqkbnr/pppp1ppp/8/4p3/2P5/8/PP1PPPPP/RNBQKBNR w KQkq - 0 2": [
        "b1c3", "g1f3", "g2g3", "e2e3", "d2d3", "h2h3", "a2a3", "f2f4", "d2d4", "e2e4"
    ],
    
    # Reti Opening (1.Nf3 d5)
    "rnbqkbnr/ppp1pppp/8/3p4/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 0 2": [
        "g2g3", "d2d4", "c2c4", "e2e3", "b2b3", "f3e5", "h2h3", "a2a3", "c1g5", "d1d2"
    ],
    
    # Bird's Opening (1.f4)
    "rnbqkbnr/pppppppp/8/8/5P2/8/PPPPP1PP/RNBQKBNR b KQkq - 0 1": [
        "d7d5", "g7g6", "e7e5", "g8f6", "c7c5", "b7b6", "e7e6", "d7d6", "a7a6", "h7h6"
    ],
    
    # King's Indian Attack (1.Nf3 d5 2.g3)
    "rnbqkbnr/ppp1pppp/8/3p4/8/5NP1/PPPPPP1P/RNBQKB1R b KQkq - 0 2": [
        "g8f6", "c7c5", "e7e6", "c7c6", "b7b6", "g7g6", "d5d4", "c8g4", "h7h6", "a7a6"
    ],
    
    # Additional positions and variations...
    # Sicilian Najdorf (1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6)
    "rnbqkb1r/1p1ppppp/p4n2/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq - 0 6": [
        "f1e2", "g1e2", "f3g5", "c1e3", "f2f4", "g2g3", "h2h3", "a2a3", "d1d2", "c3d5"
    ],
    
    # Ruy Lopez (1.e4 e5 2.Nf3 Nc6 3.Bb5)
    "r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3": [
        "a7a6", "g8f6", "d7d6", "f7f5", "b7b5", "g7g6", "d7d5", "f8c5", "f8b4", "f8e7"
    ],
    
    # Italian Game (1.e4 e5 2.Nf3 Nc6 3.Bc4)
    "r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3": [
        "f8c5", "g8f6", "d7d6", "f7f5", "b7b5", "g7g6", "h7h6", "a7a6", "d7d5", "f8e7"
    ],
    
    # Scotch Game (1.e4 e5 2.Nf3 Nc6 3.d4)
    "r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq - 0 3": [
        "e5d4", "f8b4", "g8f6", "d7d6", "f7f5", "g7g6", "h7h6", "a7a6", "d7d5", "f8c5"
    ],
    
    # Four Knights Game (1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6)
    "r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/2N2N2/PPPP1PPP/R1BQKB1R w KQkq - 4 4": [
        "f1b5", "d2d4", "f3e5", "g2g3", "h2h3", "a2a3", "f1c4", "d2d3", "c1g5", "d1e2"
    ],
    
    # Additional positions can be added following the same pattern...
    # French Winawer (1.e4 e6 2.d4 d5 3.Nc3 Bb4)
    "rnbqk1nr/ppp2ppp/4p3/3p4/1b1PP3/2N5/PPP2PPP/R1BQKBNR w KQkq - 2 4": [
        "e4e5", "a2a3", "g1f3", "d1g4", "c1d2", "f2f3", "g2g3", "h2h3", "d1d3", "f1d3"
    ],
    
    # Caro-Kann Advance (1.e4 c6 2.d4 d5 3.e5)
    "rnbqkbnr/pp2pppp/2p5/3pP3/3P4/8/PPP2PPP/RNBQKBNR b KQkq - 0 3": [
        "c8f5", "f7f6", "e7e6", "g8e7", "b7b5", "h7h5", "a7a5", "c6c5", "g7g6", "h7h6"
    ],
    
    # Pirc Defense (1.e4 d6 2.d4 Nf6 3.Nc3 g6)
    "rnbqkb1r/ppp1pp1p/3p1np1/8/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq - 0 4": [
        "g1f3", "f2f4", "f1e2", "c1e3", "h2h3", "g2g3", "a2a3", "d1d2", "f1c4", "g1e2"
    ],
    
    # Scandinavian Main Line (1.e4 d5 2.exd5 Qxd5 3.Nc3)
    "rnb1kbnr/ppp1pppp/8/3q4/8/2N5/PPPP1PPP/R1BQKBNR b KQkq - 1 3": [
        "d5a5", "d5d6", "d5d8", "g8f6", "c7c6", "e7e5", "c8g4", "b7b5", "a7a6", "h7h6"
    ],
    
    # Alekhine's Defense Four Pawns Attack (1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.c4 Nb6 5.f4)
    "rnbqkb1r/ppp1pppp/1n6/3pP3/2PP1P2/8/PP4PP/RNBQKBNR b KQkq - 0 5": [
        "d6e5", "g7g6", "e7e6", "c7c6", "c8g4", "f7f6", "b8c6", "a7a5", "h7h6", "f8e7"
    ],
    
    # Queen's Gambit Accepted (1.d4 d5 2.c4 dxc4)
    "rnbqkbnr/ppp1pppp/8/8/2pP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3": [
        "e2e3", "e2e4", "g1f3", "b1c3", "a2a4", "g2g3", "f2f3", "h2h3", "c1e3", "d1a4"
    ],
    
    # Queen's Gambit Declined (1.d4 d5 2.c4 e6)
    "rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3": [
        "b1c3", "g1f3", "c4d5", "e2e3", "g2g3", "f2f3", "h2h3", "a2a3", "c1g5", "d1b3"
    ],
    
    # Slav Main Line (1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4)
    "rnbqkb1r/pp2pppp/2p2n2/8/2pP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq - 0 5": [
        "a2a4", "e2e3", "e2e4", "g2g3", "h2h3", "a2a3", "c1g5", "d1c2", "f3e5", "c3b5"
    ],
    
    # King's Indian Main Line (1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O)
    "rnbq1rk1/ppp1ppbp/3p1np1/8/2PPP3/2N2N2/PP3PPP/R1BQKB1R w KQ - 2 6": [
        "f1e2", "h2h3", "c1e3", "f1d3", "d1d2", "a2a3", "g2g3", "f3e1", "f3d2", "c3b5"
    ],
    
    # Nimzo-Indian Classical (1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2)
    "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N5/PPQ1PPPP/R1B1KBNR b KQkq - 3 4": [
        "e8g8", "c7c5", "d7d5", "b4c3", "b7b6", "d7d6", "a7a5", "h7h6", "c8d7", "f6e4"
    ],
    
    # Grünfeld Exchange (1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.cxd5 Nxd5 5.e4 Nxc3 6.bxc3)
    "rnbqkb1r/ppp1pp1p/6p1/8/3PP3/2P5/P4PPP/R1BQKBNR b KQkq - 0 6": [
        "f8g7", "c7c5", "b7b6", "e7e5", "c8g4", "d7d6", "a7a5", "h7h6", "b8c6", "e8g8"
    ],
    
    # Benko Gambit (1.d4 Nf6 2.c4 c5 3.d5 b5)
    "rnbqkb1r/pp1ppppp/5n2/2pP4/1P6/8/P1P1PPPP/RNBQKBNR w KQkq - 0 4": [
        "c4b5", "g1f3", "b1c3", "e2e3", "g2g3", "f2f3", "h2h3", "a2a3", "c1g5", "d1c2"
    ],
    
    # Dutch Stonewall (1.d4 f5 2.g3 Nf6 3.Bg2 e6 4.c4 c6 5.Nf3 d5)
    "rnbq1rk1/pp3ppp/2p1pn2/3p4/2PP4/5NP1/PP2PPBP/RNBQK2R w KQ - 0 6": [
        "b1c3", "e1g1", "d1c2", "c1f4", "e2e3", "h2h3", "a2a3", "f3e5", "c4c5", "d1b3"
    ],
    
    # English Symmetrical (1.c4 c5)
    "rnbqkbnr/pp1ppppp/8/2p5/2P5/8/PP1PPPPP/RNBQKBNR w KQkq - 0 2": [
        "b1c3", "g1f3", "g2g3", "e2e3", "d2d3", "h2h3", "a2a3", "f2f4", "d2d4", "e2e4"
    ],
    
    # English Four Knights (1.c4 e5 2.Nc3 Nf6 3.Nf3 Nc6)
    "r1bqkb1r/pppp1ppp/2n2n2/4p3/2P5/2N2N2/PP1PPPPP/R1BQKB1R w KQkq - 4 4": [
        "g2g3", "d2d3", "e2e3", "h2h3", "a2a3", "f3e5", "c1g5", "d1c2", "e2e4", "f1b5"
    ],
    
    # Reti Accepted (1.Nf3 d5 2.c4 dxc4)
    "rnbqkbnr/ppp1pppp/8/8/2p5/5N2/PP1PPPPP/RNBQKB1R w KQkq - 0 3": [
        "e2e3", "e2e4", "b1c3", "g2g3", "h2h3", "a2a3", "d1a4", "d2d4", "f3g5", "c1e3"
    ],
    
    # King's Indian Attack vs French (1.Nf3 d5 2.g3 c5 3.Bg2 Nc6 4.O-O e6 5.d3 Nf6 6.Nbd2 Be7)
    "r1bqk2r/pp1p1ppp/2n1pn2/2p5/8/3P1NP1/PPPNPPBP/R2QK2R w KQkq - 2 7": [
        "e2e4", "e1e1", "b2b3", "h2h3", "a2a3", "c2c3", "d1e2", "f3e5", "c1e3", "f1d1"
    ],
    
    # Bird's Opening From's Gambit (1.f4 e5)
    "rnbqkbnr/pppp1ppp/8/4p3/5P2/8/PPPPP1PP/RNBQKBNR w KQkq - 0 2": [
        "f4e5", "g1f3", "e2e3", "d2d3", "b2b3", "h2h3", "a2a3", "c2c3", "f1c4", "d1f3"
    ],
    
    # Many more positions can be added following this pattern...
    # To reach hundreds of positions, you would continue adding more FEN strings
    # with their corresponding move lists in UCI format
}