import { Component, OnInit, Input } from '@angular/core';
import { AuthentificationService, User } from '../../services/authentification.service'
@Component({
  selector: 'app-edit-user',
  templateUrl: './edit-user.component.html',
  styleUrls: ['./edit-user.component.css']
})
export class EditUserComponent implements OnInit {
  user:User;
  constructor(private authService: AuthentificationService) { }

  ngOnInit() {
    this.user = this.authService.authInfo.user;
  }
  save() {
    this.authService.saveUser(this.user).subscribe(user => {
      this.authService.authInfo.user = user;
      this.user = user;
    },
      error => {
        console.log('Cannot login !!!');
      }
    );
  }
  reset() {
    this.authService.getUser().subscribe(user => {
      this.authService.authInfo.user = user;
      this.user = user;
    },
      error => {
        console.log('Cannot login !!!');
      }
    );
  }

}
