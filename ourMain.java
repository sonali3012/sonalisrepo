package Interface_classes;

/*
Create an interface Playable with a method play().
Create two classes VideoGame and MusicPlayer that implement Playable in their own way.
Instantiate both and call play().
 */

 interface Playable {
    void play();
}

class VideoGame implements Playable {
    public void play() {
        System.out.println("Video games can be played by any aged users");
    }  
}

class MusicPlayer implements Playable {
    public void play() {
        System.out.println("Music players are so old now");
    }
}

public class ourMain {
    public static void main(String[] args) {
        Playable videoGame = new VideoGame();
        videoGame.play();

        Playable musicPlayer = new MusicPlayer();
        musicPlayer.play();
    }
}




