import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ModalModule } from 'ngx-bootstrap/modal';
import { FormsModule } from '@angular/forms';

import { WorkspaceComponent } from './workspace.component';
import { WorkspaceListComponent } from './workspace-list/workspace-list.component';
import { WorkspaceRoutingModule } from './workspace-routing.module';

@NgModule({
  imports: [
    CommonModule, WorkspaceRoutingModule, ModalModule.forRoot(), FormsModule

  ],
  declarations: [WorkspaceComponent, WorkspaceListComponent]
})
export class WorkspaceModule { }
