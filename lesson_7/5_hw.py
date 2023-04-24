import time
from abc import ABC, abstractmethod
from dataclasses import dataclass


class TimeTeller:
    def __init__(self, h=None, m=None, s=None) -> None:
        """Recieves all hours, minutes and seconds attributes and
        makes object with given time or reads current system time."""
        if h and m and s:
            self.h = h
            self.m = m
            self.s = s
        else:
            time_t = time.localtime()
            self.h = time_t.tm_hour
            self.m = time_t.tm_min
            self.s = time_t.tm_sec
            """
            alternatively
            time_t = time.ctime()[-13:-5]
            self.h, self.m, self.s = tuple(map(int, time_t.split(':')))
            """

    def __str__(self):
        """Print operation."""
        return f"{self.h}:{self.m}:{self.s}"

    def seconds_pass(self):
        """Function gives converts normalized time to just seconds."""
        return self.s + self.m * 60 + self.h * 3600

    def __eq__(self, other) -> bool:  # ==
        return self.seconds_pass() == other.seconds_pass()

    def __ne__(self, other) -> bool:  # !=
        return self.seconds_pass() != other.seconds_pass()

    def __lt__(self, other) -> bool:  # <
        return self.seconds_pass() < other.seconds_pass()

    def __gt__(self, other) -> bool:  # >
        return self.seconds_pass() > other.seconds_pass()

    def __le__(self, other) -> bool:  # <=
        return self.seconds_pass() <= other.seconds_pass()

    def __ge__(self, other) -> bool:  # >=
        return self.seconds_pass() >= other.seconds_pass()


@dataclass
class Post:
    message: str
    timestamp: TimeTeller


class SocialChannel(ABC):
    @abstractmethod
    def download_post():
        ...


class YouTube(SocialChannel):
    def download_post(self, post) -> None:
        print(f"--{post.message}--\nPosted on YouTube at {post.timestamp}!\n")


class Facebook(SocialChannel):
    def download_post(self, post) -> None:
        print(f"--{post.message}--\nPosted on Facebook at {post.timestamp}!\n")


class Twitter(SocialChannel):
    def download_post(self, post) -> None:
        print(f"--{post.message}--\nPosted on Twitter at {post.timestamp}!\n")


class PostingProcessor:
    def __init__(self, channel: SocialChannel) -> None:
        self._channel = channel

    def post_a_message(self, post: Post) -> None:
        self._channel.download_post(post)


def post_channel_dispatcher(decision: str) -> SocialChannel:
    """Returns corresponding channel object. Doesn`t check for wrong input."""
    if decision.lower() == "youtube":
        return YouTube()
    if decision.lower() == "facebook":
        return Facebook()
    if decision.lower() == "twitter":
        return Twitter()


def post_a_message(channel: str, post: Post):
    """Function calls channel`s method for posting."""
    post_channel: SocialChannel = post_channel_dispatcher(channel)

    post_processor = PostingProcessor(post_channel)
    post_processor.post_a_message(post)


def process_schedule(posts: list[Post], channels: list[str]) -> None:
    """Function checkes timestamps and sends or schedules posts."""
    for post in posts:
        for channel in channels:
            if post.timestamp <= TimeTeller():
                post_a_message(channel, post)
            else:
                print(f"Post '{post.message}' scheduled for {post.timestamp}")


def main():
    print("===SIMPLE POSTS===")
    youtube_post = Post("YouTube is great!", TimeTeller())
    post_a_message("youtube", youtube_post)

    facebook_post = Post("Facebook is awesome!", TimeTeller())
    post_a_message("Facebook", facebook_post)

    twitter_post = Post("Twitter is amazing!", TimeTeller())
    post_a_message("twitter", twitter_post)

    print("===SCHEDULED===")
    post_1 = Post("Post_1 scheduled NOW.", TimeTeller())
    post_2 = Post("Post_2 scheduled LATER.", TimeTeller(23, 59, 59))
    post_3 = Post("Post_3 scheduled NOW.", TimeTeller())
    process_schedule([post_1, post_2, post_3], ["youtube", "twitter"])


if __name__ == "__main__":
    main()
