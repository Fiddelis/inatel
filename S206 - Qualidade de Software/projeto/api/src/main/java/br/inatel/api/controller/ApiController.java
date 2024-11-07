package br.inatel.api.controller;

import br.inatel.api.model.User;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api")
public class ApiController {

    private User user;
    private final Map<String, String> errorResponse = new HashMap<>();

    @PostMapping
    public ResponseEntity<Object> postUser(@RequestBody User userResponse) {
        if(userResponse.getName() == null) {
            errorResponse.put("erro", "usuario não pode ser nulo");
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(errorResponse);
        }
        user = userResponse;
        return ResponseEntity.ok(user);
    }

    @GetMapping
    public ResponseEntity<Object> getUser() {
        if(user == null) {
            errorResponse.put("erro", "nenhum usuario encontrado");
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(errorResponse);
        }
        return ResponseEntity.ok(user);
    }

    @DeleteMapping
    public ResponseEntity<Object> deleteUser() {
        if(user == null) {
            errorResponse.put("erro", "nenhum usuario encontrado");
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(errorResponse);
        }
        user = null;

        return ResponseEntity.ok(null);
    }
}
