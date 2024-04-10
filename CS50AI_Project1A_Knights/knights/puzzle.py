from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    
    #Game Logic, has to be either and cannot be both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    Implication(AKnight, And(AKnight, AKnave)), #if knight, A has to be true
    Implication(AKnave, Not(And(AKnave, AKnight))), #if knave A has to be false

)   
# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    #Game Logic, has to be either and cannot be both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

    #Statements
    #if A knight, then statement true tf:
    Implication(AKnight, And(AKnave, BKnave)), 
    #if knave, statement is false, tf: 
    Implication(AKnave, Not(And(AKnave, BKnave)))
        
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    #Game Logic, has to be either and cannot be both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

    #if A is  a Knave, then statement doesn't hold. TF: they are not the same
    Implication(AKnave, Not(Or(And(AKnave, BKnave), And(AKnight, BKnight)))),
    #If A is a knight, then statement holds. TF: have to be the same
    Implication(AKnight, Or(And(AKnight, BKnight),And(AKnave, BKnave))),
    #If B is Knave, statemnt is false. TF: A&B have to be same 
    Implication(BKnave, Or(And(AKnave, BKnave), And(AKnight, BKnight))),
    #If B is knight, statemnt holds. TF: A&B have to be different
    Implication(BKnight, Not(Or(And(AKnave, BKnave), (And(AKnight, BKnight)))))
                
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    #Game Logic, has to be either and cannot be both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),

    #B Logic 

    #if knight, logic is true. TF: C = Knave, A said 'I am a kanve'
    Implication(BKnight, CKnave),
    Implication(BKnight, And(
        # A said I'm a Knave, could be either
        Implication(AKnight, AKnave),
        Implication(AKnave, Not(AKnave))
    )),
    #If Knave, logic is false, TF: C is a knight and A did not say 'I am knave'
    Implication(BKnave, CKnight),
    Implication(BKnave, And(
        Implication(AKnight, AKnight),
        Implication(AKnave, Not(AKnight)),
    )),
    #C logic

    #If C knight, statement True. TF: A is knight 
    Implication(CKnight, AKnight),
    #if C Knave, statement False. TF A is Knave
    Implication(CKnave, Not(AKnight)),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
