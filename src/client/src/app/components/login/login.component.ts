import { Component, OnInit, Input } from '@angular/core';
import { AuthentificationService } from '../../services/authentification.service'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  email: string;
  password: string;
  constructor(private authService: AuthentificationService) { }

  ngOnInit() {
  }
  login() {
    this.authService.login(this.email, this.password).subscribe(info => {
      this.authService.setInfo(info);
    },
    error => {
        console.log('Cannot login !!!');
      }
    );
  }
}
