import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpModule } from '@angular/http';
import { AuthentificationService } from './authentification.service';
import { WorkspaceService } from './workspace.service';
import { UserFieldGroupService } from './user-field-group.service';

@NgModule({
  imports: [
    CommonModule, HttpModule
  ],
  declarations: [],
  providers: [AuthentificationService, WorkspaceService, UserFieldGroupService]
})
export class ServicesModule { }
