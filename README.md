# Automated-Content-Management-System
Aggregate and recombine Metacritic (www.metacritic.com) information to visualized and reinterpret valuable and readable data that reflects the current state of the game industry
# <img width="186" alt="image" src="https://user-images.githubusercontent.com/113169589/227984151-822c14eb-783f-4427-8c43-a512f893905d.png"> 
[Metacritic](http://www.metacritic.com) is a website that aggregates reviews of films, television shows, music albums, video games, and formerly books.
Due to its large quantity of high-quality rating data and multiple dimensions, it has good research value.


:joystick: In AIDM 7360 Group Project, we mainly focus on the game rating.This repository provides specific web-crawling code and some data acquisition processes, different web-crawling code files target different webpage content.

- Spider_every_year.py & Spider_every_game.py 
&emsp;
> For example, in 2023, by crawling all the URLs of each game in 2023 through the previous web page, visit and crawl further related data for each game URL.
> The game data we crawl includes but is not limited to the following:
&emsp;
<div align=center>
<img src="https://user-images.githubusercontent.com/113169589/227991570-a37f57fd-258c-4d1c-9af4-0045ef8a7d97.png" width="500px">
</div>


- every_critic_new.py

> By accessing all media review page tags, obtain the ratings and evaluations of the game from the media and related individuals.

&emsp;

<div align=center>
<img src="https://user-images.githubusercontent.com/113169589/227995033-f7786011-b0b6-4fa4-afd2-9a4fb5195055.png" width="600px">
 </div>
&emsp;
<div align=center>
<img src="https://user-images.githubusercontent.com/113169589/227997523-2280cd01-f2fe-4a1a-80dc-8e00b077934f.png" width="600px">
   </div>
   
&emsp;

_In actual operation, some code will be slightly adjusted_
