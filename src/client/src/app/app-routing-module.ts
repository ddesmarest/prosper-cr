import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { EditUserComponent } from './components/edit-user/edit-user.component';
import { PageNotFoundComponent } from './components/page-not-found/page-not-found.component';
import { WelcomeComponent } from './components/welcome/welcome.component';
import { WorkspaceComponent } from './workspace/workspace.component';


export const appRoutes: Routes = [
    {
        path:'workspace', component:WorkspaceComponent
    },
    {
        path: 'edit-user', component: EditUserComponent
    },
    {
        path: 'welcome', component: WelcomeComponent
    },
    
    { path: '', redirectTo: '/welcome', pathMatch: 'full' },
    { path: '**', component: PageNotFoundComponent }
];
@NgModule({    
    exports: [ RouterModule ]
  })
  export class AppRoutingModule {}
  