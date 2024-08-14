opcodes = {
    "NO opcode": 0b0000,
    "Prog": 0b0001,
    "ProgStream": 0b0011,
    "A_ADD": 0b0100,
    "A_SUB": 0b0101,
    "A_MUL": 0b0010,
    "A_DIV": 0b0110,
    "A_ADDS": 0b0111,
    "A_SUBS": 0b1000,
    "A_MULS": 0b1001,
    "A_DIVS": 0b1010,
    "Av_ADDS": 0b1011,
    "CMPS": 0b1100,
    "UPDATE": 0b1101,
    "EQUALS": 0b0010
}

# BIT LOCATION PARAMETERS
opCodeWidth = 4
addressWidth = 12
FOpWidth = 32
LCWidth = 10
opStrtLoc = 0
wordSizeFP = 64
seqWidth = 6
opEndLoc = (opStrtLoc + opCodeWidth -1)
destStrtLoc = (opEndLoc+1)
destEndLoc = (destStrtLoc +addressWidth-1)
valStrtLoc = (destEndLoc+1)
valEndLoc = (valStrtLoc+FOpWidth-1)
nextOPStrtLoc = (valEndLoc+1)
nextOPEndLoc = (nextOPStrtLoc+opCodeWidth-1)
nextDestStrtLoc = (nextOPEndLoc+1)
nextDestEndLoc = (nextDestStrtLoc+addressWidth-1)
strAdd1StrtLoc = (destEndLoc+1)
strAdd1EndLoc = (strAdd1StrtLoc+addressWidth-1)
strFlag1 = (strAdd1EndLoc+1)
seqTrans = (strFlag1+1)
nextLCStrtLoc = ((seqTrans+1))
nextLCEndLoc = ((nextLCStrtLoc+LCWidth -1))
unUsedStrtLoc = ((nextLCEndLoc+1))
unUsedEndLoc = ((wordSizeFP-1))
LCStrtLoc = (valEndLoc+1)
LCEndLoc = (LCStrtLoc+LCWidth-1)
seqStrtLoc = (LCEndLoc+1)
seqEndLoc = (seqStrtLoc+seqWidth-1)
