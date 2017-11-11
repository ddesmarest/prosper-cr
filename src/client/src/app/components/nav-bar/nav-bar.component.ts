import { Component, OnInit } from '@angular/core';
import { AuthentificationService,User } from '../../services/authentification.service'
@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent implements OnInit {
  user:User;
  constructor(private authService: AuthentificationService) { }

  ngOnInit() {
    this.user = this.authService.authInfo.user;
  }
  logout() {
    this.authService.setInfo({token:'',user:null})
  }

}
