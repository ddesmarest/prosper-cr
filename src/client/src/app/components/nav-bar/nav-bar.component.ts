import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthentificationService,User } from '../../services/authentification.service'
import { WorkspaceService, Workspace } from '../../services/workspace.service';
@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent implements OnInit {
  user:User;
  currentWorkspace:Workspace;
  workspaces:Array<Workspace>;
  constructor(private authService: AuthentificationService, private worskspaceService:WorkspaceService, private router:Router) { 
    this.worskspaceService.getWorkspaces().subscribe(workspaces => {
      this.workspaces = workspaces
      if( this.workspaces.length != 0) {
        this.selectWorkspace( this.workspaces[0]);
      }
    });
  }

  ngOnInit() {
    this.user = this.authService.authInfo.user;
  }
  logout() {
    this.authService.setInfo({token:'',user:null})
  }
  selectWorkspace(workspace:Workspace) {
    this.currentWorkspace = workspace;
    this.router.navigate(['/']);
  }
}
