import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ModalModule } from 'ngx-bootstrap/modal';
import { AccordionModule } from 'ngx-bootstrap/accordion';
import { WorkspaceComponent } from './workspace.component';
import { WorkspaceListComponent } from './workspace-list/workspace-list.component';
import { WorkspaceRoutingModule } from './workspace-routing.module';
import { WorkspaceEditionComponent } from './workspace-edition/workspace-edition.component';

@NgModule({
  imports: [
    CommonModule, WorkspaceRoutingModule, ModalModule.forRoot(), FormsModule,AccordionModule.forRoot()

  ],
  declarations: [WorkspaceComponent, WorkspaceListComponent, WorkspaceEditionComponent]
})
export class WorkspaceModule { }
