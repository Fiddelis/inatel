import com.intuit.karate.junit5.Karate;

public class ExampleTest {
    @Karate.Test
    Karate test() {
        return Karate.run("classpath:example.feature").relativeTo(getClass());
    }
}
