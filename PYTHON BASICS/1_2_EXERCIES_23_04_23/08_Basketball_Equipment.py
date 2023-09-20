basketball_yearly_tax = int(input())

basketball_shoes = basketball_yearly_tax * 0.40
price_basketball_shoes = basketball_yearly_tax - basketball_shoes

basketball_outfit = price_basketball_shoes * 0.20
price_basketball_outfit = price_basketball_shoes - basketball_outfit

price_basketball_ball = price_basketball_outfit * 0.25

price_basketball_accessories = price_basketball_ball * 0.20

total_cost_for_training = basketball_yearly_tax + price_basketball_shoes \
                          + price_basketball_outfit + price_basketball_ball\
                          + price_basketball_accessories

print(total_cost_for_training)
