select(gapminder, year, country, gdpPercap)
filter(gapminder, continent=="Europe")

gapminderEurope <- filter(gapminder, continent=="Europe")

select(gapminderEurope, year, country, gdpPercap)

gapminderEuropeGDP <- gapminder %>% filter(continent == "Europe") %>% select(year, country, gdpPercap)

gapminderAfricaLifeExp <- gapminder %>% filter(continent == "Africa") %>% select(lifeExp, country, year)

gapminder %>% filter(continent == "Europe", year == 2007) %>% arrange(desc(pop))

gapminder %>% mutate(gdp = pop * gdpPercap)

gapminderLifeExpEuropeHigh <- gapminder %>% filter(continent == 'Europe', year == 2007) %>% arrange(desc(lifeExp)) %>% mutate(rank = row_number())

gapminderLifeExpEuropeHigh

gapminderLifeExpEuropeLow <- gapminder %>% filter(continent == 'Europe', year == 2007) %>% arrange((lifeExp)) %>% mutate(rank = row_number())

gapminderLifeExpEuropeLow

gapminder %>%  filter(year == 2007) %>% 
  summarise(meanLife = mean(lifeExp), medianLife = median(lifeExp))

gapminder %>%  filter(year == 2007) %>% 
  group_by(continent) %>% 
  summarise(meanLife = mean(lifeExp), medianLife = median(lifeExp))

lifeExpByContinentByYear <- gapminder %>% group_by(continent, year) %>% 
  summarise(meanLife = mean(lifeExp))