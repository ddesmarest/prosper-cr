import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

import { WorkspaceService, Workspace } from '../../services/workspace.service';
import { UserFieldGroup, UserFieldGroupService } from '../../services/user-field-group.service';

@Component({
  selector: 'app-workspace-edition',
  templateUrl: './workspace-edition.component.html',
  styleUrls: ['./workspace-edition.component.css']
})
export class WorkspaceEditionComponent implements OnInit {
  workspace: Workspace;

  constructor(private route: ActivatedRoute, private workspaceService: WorkspaceService,
    private userFieldGroupService: UserFieldGroupService) { }

  ngOnInit() {
    this.workspaceService.getWorkspace(this.route.snapshot.paramMap.get('id')).subscribe(workspace => this.workspace = workspace);
  }
  openOrCloseGroup(isOpen: boolean, group: UserFieldGroup) {
    if (this.workspace && isOpen) {
      this.userFieldGroupService.getUserFieldGroups(this.workspace).subscribe(groups=>this.updateFieldGroups(groups));
      console.log('Opened !!!');
    }
  }
  updateFieldGroups(groups:Array<UserFieldGroup>) {
    for(let i = 0 ;i< groups.length;++i) {
      this.workspace.field_groups[i].fields = groups[i].fields;
    }
  }
}
