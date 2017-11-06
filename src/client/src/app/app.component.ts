import { Component } from '@angular/core';
import { AuthentificationService } from './services/authentification.service'

import { LoginComponent } from './components/login/login.component'
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Prosper CR';
  constructor(private authService: AuthentificationService) {    
  }
  ngOnInit() {
    this.authService.verify()
  }
  should_login():boolean {
    return this.authService.authInfo.token == '';
  }
}
