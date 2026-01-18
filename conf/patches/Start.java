import java.io.File;
import java.util.Arrays;
import net.minecraft.client.main.Main;

public class Start {
    public static void main(String[] args) {
        // Cấu hình đường dẫn Natives để nhận LWJGL 3.3.3
        System.setProperty("java.library.path", "jars/versions/1.13/1.13-natives");

        String[] defaultArgs = new String[] {
            "--version", "1.13",
            "--accessToken", "0",
            "--assetsDir", "jars/assets",
            "--assetIndex", "1.13",
            "--userProperties", "{}",
            "--gameDir", "jars"
        };

        String[] combinedArgs = new String[defaultArgs.length + args.length];
        System.arraycopy(defaultArgs, 0, combinedArgs, 0, defaultArgs.length);
        System.arraycopy(args, 0, combinedArgs, defaultArgs.length, args.length);

        Main.main(combinedArgs);
    }
}