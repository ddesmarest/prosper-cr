import { Component, OnInit } from '@angular/core';
import { AuthentificationService, User } from '../../services/authentification.service'

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {
  user:User=null;
  constructor(private authService: AuthentificationService) { }

  ngOnInit() {
    this.user = this.authService.authInfo.user;
  }

}
