import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.stage.Stage;

public class Hello extends Application {

	@Override
	public void start(Stage primaryStage) throws Exception {
        primaryStage.setTitle("Solid Pre");

        Label label = new Label("Uy Walang Error");
        //Since only 1 scene size of stage has been resized to 400, 200(h)
        Scene scene = new Scene(label, 400, 200);
        primaryStage.setScene(scene);

        primaryStage.show();
    }

    public static void main(String[] args) {
        Application.launch(args);
    }
}