import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { WorkspaceComponent } from './workspace.component';
import { WorkspaceListComponent }       from './workspace-list/workspace-list.component';
import { WorkspaceEditionComponent }       from './workspace-edition/workspace-edition.component';
/*import { CrisisCenterComponent }     from './crisis-center.component';
import { CrisisDetailComponent }     from './crisis-detail.component';*/

const workspaceRoutes: Routes = [
  {
    path: 'workspace',
    component: WorkspaceComponent,
    children: [
      {
        path: '',
        component: WorkspaceListComponent
        /*,
        children: [
          {
            path: ':id',
            component: CrisisDetailComponent
          },
          {
            path: '',
            component: CrisisCenterHomeComponent
          }
        ]*/
      },
      {
        path:':id',
        component: WorkspaceEditionComponent
      }
    ]
  }
];

@NgModule({
  imports: [
    RouterModule.forChild(workspaceRoutes)
  ],
  exports: [
    RouterModule
  ]
})
export class WorkspaceRoutingModule { }