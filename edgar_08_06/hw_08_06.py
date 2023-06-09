'''
1․ Գրել MyShows class, որը․
   - __init__ ում կստանա 
     -- սերիալի անունը (պետք է լինի տեքստ), 
     -- հարթակը, որտեղ ցուցադրվում է սերիալը (պետք է լինի տեքստ), 
     -- առաջին սերիան դուրս գալու տարեթիվը (պետք է լինի ամբողջ թիվ),
     -- սերիայի համարը, որը դիտում է օգտատերը (որ սերիային է հասել) 
     (պետք է լինի ամբողջ թիվ), default արժեքը պետք է լինի 0,
     -- օգտատիրոջ դրած գնահատականը (պետք է լինի ամբողջ թիվ 
     1-10 միջակայքում), default արժեքը պետք է լինի None,
     -- գլխավոր դերասանների ցանկը (պետք է լինի լիստ),
   - բոլոր ատրիբուտները կլինեն private,
   - կունենա getter բոլոր ատրիբուտների համար,
   - միայն սերիայի համարի և գնահատականի համար կունենա նաև setter,
   - միայն գնահատականի համար կունենա նաև deleter, այնպես պետք է 
   ռեալիզացնել, որ գնահատականը ջնջելուց հետո այն նորից սահմանելու 
   հնարավորություն լինի,
   - կունենա մեթոդներ դերասանների ցանկը թարմացնելու համար (լիստից 
   անուն ջնջել, լիստում անուն ավելացնել),
   - կունենա մեթոդ, որը կվերադարձնի սերիալի մասին ամբողջ ինֆորմացիան։
'''

class MyShows:
    def __init__(self, show_name: str, streaming_service: str, start_year: int,
                 cast: list, episode: int = 0, rating: int = None):
        if self.is_valid_text(show_name) and self.is_valid_text(streaming_service) and \
            self.is_valid_year(start_year) and self.is_valid_cast(cast) and \
            self.is_valid_episode(episode) and self.is_valid_rating(rating):
            
            self.__show_name = show_name
            self.__streaming_service = streaming_service
            self.__start_year = start_year
            self.__cast = cast
            self.__episode = episode
            self.__rating = rating
        else:
            raise Exception("Invalid show attributes")

    @staticmethod
    def is_valid_text(text):
        return isinstance(text, str) and len(text) > 0
    
    @staticmethod
    def is_valid_year(year):
        return isinstance(year, int) and year >= 1900
    
    @staticmethod
    def is_valid_episode(episode):
        return isinstance(episode, int) and episode >= 0
    
    @staticmethod
    def is_valid_rating(rate):
        if isinstance(rate, int):
            return 1 <= rate <= 10
        else:
            return rate is None
    
    @staticmethod
    def is_valid_cast(cast):
        return isinstance(cast, list) and len(cast) > 0 \
              and len(cast) == sum(map(lambda x: isinstance(x, str) and len(x) > 0, cast))
    
    @property
    def show_name(self):
        return self.__show_name
    
    @property
    def streaming_service(self):
        return self.__streaming_service
    
    @property
    def start_year(self):
        return self.__start_year
    
    @property
    def cast(self):
        return self.__cast
    
    @property
    def episode(self):
        return self.__episode
    
    @episode.setter
    def episode(self, ep):
        if self.is_valid_episode(ep):
            self.__episode = ep
        else:
            raise Exception("Invalid Episode")
    
    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, rate):
        if self.is_valid_rating(rate):
            self.__rating = rate
        else:
            raise Exception("Invalid Rating")
        
    @rating.deleter
    def rating(self):
        self.__rating = None

    def add_actor(self, actor):
        if self.is_valid_text(actor):
            self.__cast.append(actor)
        elif self.is_valid_cast(actor):
            self.__cast.extend(actor)
            # self.__cast = list(set(self.__cast))
        else:
            raise Exception("Invalid Actor")
        
    def remove_actor(self, actor):
        if self.is_valid_text(actor) and actor in self.__cast:
            self.__cast.remove(actor)
        elif self.is_valid_cast(actor):
            for item in actor:
                if item in self.__cast:
                    self.__cast.remove(item)
        else:
            raise Exception("Invalid actor(s)")
        
    def __str__(self) -> str:
        return f"{self.show_name}, {self.streaming_service}, {self.start_year}," +\
                f"{self.cast}, {self.episode}, {self.rating}"

            


    
show = MyShows("Narcos", "Netflix", 2015, ["Pedro Pascal"])
print(show.show_name)
print(show.streaming_service)
print(show.start_year)
print(show.cast)
print(show.episode)
print(show.rating, end="\n\n")

show.episode = 7
print(show.episode)
show.rating = 9
print(show.rating, end="\n\n")

del show.rating
print(show.rating, end="\n\n")

show.add_actor("Boyd Holbrook")
show.add_actor(["Wagner Moura", "Diego Luna"])
print(show.cast, end="\n\n")
show.remove_actor("Boyd Holbrook")
show.remove_actor(["Wagner Moura", "Diego Luna", "a"])
print(show.cast, end="\n\n")

print(show)
