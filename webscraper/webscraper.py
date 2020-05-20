from bs4 import BeautifulSoup
import requests
import json
import csv


year = 2016
for x in range(year,2020):
    url = 'https://www.pro-football-reference.com/years/'+str(x)+'/fantasy.htm'
    its = 1



    response = requests.get(url, timeout = 5)
    content = BeautifulSoup(response.content, 'html.parser')
    table = BeautifulSoup(str(content.select('tbody')),'html.parser')
    table_rows = table.find_all('tr')
    players = []
    for i in range(0,308):
        
        if (i==29 or i==60 or i==91 or i==122 or i==153 or i==184 or i==215 or i==246 or i==277):
            i = i+1
            its = its-1
        
        name = table_rows[i].find('td').a
        team_name = name.find_next('td')
        position = team_name.find_next('td')
        age = position.find_next('td')
        games_played = age.find_next('td')
        games_start = games_played.find_next('td')
        pass_comp = games_start.find_next('td')
        pass_att = pass_comp.find_next('td')
        pass_yrds = pass_att.find_next('td')
        pass_td = pass_yrds.find_next('td')
        pass_int = pass_td.find_next('td')
        rush_att = pass_int.find_next('td')
        rush_yds = rush_att.find_next('td')
        rush_yds_per_att = rush_yds.find_next('td')
        rush_tds = rush_yds_per_att.find_next('td')
        rec_tgt = rush_tds.find_next('td')
        rec_receptions = rec_tgt.find_next('td')
        rec_yards = rec_receptions.find_next('td')
        rec_yrds_per_reception = rec_yards.find_next('td')
        rec_tds = rec_yrds_per_reception.find_next('td')
        fumbles = rec_tds.find_next('td')
        fumbles_lost = fumbles.find_next('td')
        scoring_tds = fumbles_lost.find_next('td')
        scoring_two_point_conversation = scoring_tds.find_next('td')
        scoring_two_point_passes = scoring_two_point_conversation.find_next('td')
        fantasy_points = scoring_two_point_passes.find_next('td')
        ppr_points = fantasy_points.find_next('td')
        draft_king_points = ppr_points.find_next('td')
        fan_duel_points = draft_king_points.find_next('td')
        vbd = fan_duel_points.find_next('td')
        position_rank = vbd.find_next('td')
        overall_rank = int(position_rank.find_next('td').string) if position_rank.find_next('td').string else its
        its = its + 1
        player = {
            "name": name.string,
            "teamName": team_name.string,
            "position": position.string if position.string else 'N/A',
            "age": int(age.string),
            "gamesPlayed": int(games_played.string),
            "gamesStarted": int(games_start.string),
            "passComp": int(pass_comp.string),
            "passAtt": int(pass_att.string),
            "passYrds": int(pass_yrds.string),
            "passTds": int(pass_td.string),
            "passInts": int(pass_int.string),
            "rushAtt": int(rush_att.string),
            "rushYds": int(rush_yds.string),
            "rushYdsPerAtt": float(rush_yds_per_att.string) if rush_yds_per_att.string else 0.0,
            "rushTds": int(rush_tds.string),
            "recTgt": int(rec_tgt.string),
            "recReceptions": int(rec_receptions.string),
            "recYards": int(rec_yards.string),
            "recYdsPerAtt": float(rec_yrds_per_reception.string) if rec_yrds_per_reception.string else 0.0,
            "recTds": int(rec_tds.string),
            "fumbles": int(fumbles.string),
            "fumblesLost": int(fumbles_lost.string),
            "scoringTds": int(scoring_tds.string),
            "scoringTwoPointConversation": int(scoring_two_point_conversation.string) if scoring_two_point_conversation.string else 0,
            "scoringTwoPointPass": int(scoring_two_point_passes.string) if scoring_two_point_passes.string else 0,
            "fantasyPoints": float(fantasy_points.string) if fantasy_points.string else 0.0,
            "pprPoints": float(ppr_points.string) if ppr_points.string else 0.0,
            "draftKingPoints": float(draft_king_points.string) if ppr_points.string else 0.0,
            "fanDuelPoints": float(fan_duel_points.string) if fan_duel_points.string else 0.0,
            "vbd": int(vbd.string) if vbd.string else 0,
            "positionRank": int(position_rank.string),
            "overallRank": overall_rank
        }
        players.append(player)
    with open('fantasyStats'+str(x)+'.json', 'w') as outputfile: json.dump(players, outputfile)

