import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';

import { AuthenticatedService } from './authenticated-service';
import { AuthentificationService } from './authentification.service';

import { Workspace } from './data-model';
export { Workspace } from './data-model';

@Injectable()
export class WorkspaceService extends AuthenticatedService {

  constructor(private http: Http, authService: AuthentificationService) {
    super(authService);
  }

  getWorkspaces(): Observable<Array<Workspace>> {
    return this.http.get(this.getFullUrl('workspaces'), { headers: this.createHeaders() }).map(workspaces => workspaces.json());
  }
  deleteWorkspace(workspace: Workspace) {
    return this.http.delete(this.getFullUrl('workspaces', workspace.id), { headers: this.createHeaders() });
  }
  addWorkspace(name: string): Observable<Workspace> {
    return this.http.post(this.getFullUrl('workspaces'), { name: name }, { headers: this.createHeaders() }).map(workspace => workspace.json());
  }
  getWorkspace(id: string): Observable<Workspace> {
    return this.http.get(this.getFullUrl('workspaces', id), { headers: this.createHeaders() }).map(workspace => workspace.json());
  }
}
