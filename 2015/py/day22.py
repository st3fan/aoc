

import random


class Spell:
    def __init__(self, name, cost, duration, immediate, damage=None, heal=None, armor=None, mana=None):
        self.name = name
        self.cost = cost
        self.duration = duration
        self.immediate = immediate
        self.damage = damage
        self.heal = heal
        self.armor = armor
        self.mana = mana


SPELLS = [
    Spell("Missile",  53, 1, True,  damage=4),
    Spell("Drain",    73, 1, True,  damage=2, heal=2),
    Spell("Shield",  113, 7, False,  armor=7),
    Spell("Poison",  173, 6, False, damage=3),
    Spell("Recharg", 229, 5, False, mana=101)
]


class Player:
    def __init__(self, points):
        self.points = points
    def apply_damage(self, damage):
        self.points -= damage
        return self.points <= 0
    def turn(self):
        return None, 0


class Boss (Player):
    def __init__(self, points, damage):
        super().__init__(points)
        self.damage = damage
    def turn(self):
        return None, self.damage


class Wizard (Player):

    def __init__(self, points, mana):
        super().__init__(points)
        self.mana = mana
        self.armor = 0
        self.spent = 0

    def turn(self, active_effects):
        #return SPELLS[0], 0 # Always return Missile
        #if self.mana == 500:
        #    self.mana -= SPELLS[3].cost
        #    return SPELLS[3], 0
        #return SPELLS[0], 0
        spells = list(SPELLS)
        random.shuffle(spells)
        for spell in spells:
            if spell in [effect.spell for effect in active_effects]:
                continue
            if self.mana >= spell.cost:
                self.mana -= spell.cost
                self.spent += spell.cost
                return spell, 0
        return None, None


class Effect:
    def __init__(self, spell):
        self.spell = spell
        self.counter = spell.duration


class Game:
    def __init__(self, boss, player):
        self.boss = boss
        self.player = player
        self.current_player = "Player"
        self.effects = set()

    def turn(self):
        #print("")
        #print(f"-- {self.current_player} Turn --")
        #print(f"- Player has {self.player.points} hit points, {self.player.armor} armor, {self.player.mana} mana")
        #print(f"- Boss has {self.boss.points} hit points")

        # Apply all active effects
        for effect in self.effects:
            #print(f"{effect.spell.name}: {effect.spell.name}, damage += {effect.spell.damage}, heal += {effect.spell.heal}, armor += {effect.spell.armor}, mana += {effect.spell.mana}")
            if effect.spell.damage:
                self.boss.points -= effect.spell.damage
            if effect.spell.heal:
                self.player.points += effect.spell.heal
            if effect.spell.armor:
                self.player.armor += effect.spell.armor
            if effect.spell.mana:
                self.player.mana += effect.spell.mana
            effect.counter -= 1
            #print(f"{effect.spell.name} is now at count {effect.counter}")

        # Wear off effects
        expired = set()
        for effect in self.effects:
            if effect.counter == 0:
                expired.add(effect)
                #print(f"{effect.spell.name} wears off.")
        self.effects -= expired

        # Maybe the boss is dead from the effects
        if self.boss.points <= 0:
            #print("This kills the boss, and the player wins!")
            return True

        match self.current_player:
            case "Player":
                spell, _ = self.player.turn(self.effects) # Wizards only cast spells
                if not spell:
                    #print(f"Player ran out of money")
                    return True
                #print(f"Player casts {spell.name} (damage += {spell.damage}, heal += {spell.heal}, armor += {spell.armor}, mana += {spell.mana})")

                for effect in self.effects:
                    assert effect.spell != spell, f"Spell {effect.spell.name} already active."

                if spell.immediate:
                    #print(f"{spell.name}: {spell.name}, damage += {spell.damage}, heal += {spell.heal}, armor += {spell.armor}, mana += {spell.mana}")
                    if spell.damage:
                        if self.boss.apply_damage(spell.damage):
                            #print("This kills the boss and the player wins.")
                            return True
                    if spell.heal:
                        self.player.points += spell.heal
                    if spell.armor:
                        self.player.armor += spell.armor
                    if spell.mana:
                        self.player.mana += spell.mana

                if spell.duration != 1:
                    effect = Effect(spell)
                    #if spell.immediate:
                    #    effect.counter -= 1
                    self.effects.add(effect)

                self.current_player = "Boss"

            case "Boss":
                _, damage = self.boss.turn() # Bosses only cause damage
                actual_damage = max(damage - self.player.armor, 1)
                #print(f"Boss attacks for {damage} - {self.player.armor} = {actual_damage} damage!")
                if self.player.apply_damage(actual_damage):
                    #print("This kills the player and the boss wins.")
                    return True
                self.current_player = "Player"


def main():
    spendings = []
    for _ in range(1_000_000):
        game = Game(Boss(58, 9), Wizard(50, 500))
        while not game.turn():
            pass
        if game.boss.points <= 0:
            spendings.append(game.player.spent)
    print(min(spendings))


if __name__ == "__main__":
    main()
