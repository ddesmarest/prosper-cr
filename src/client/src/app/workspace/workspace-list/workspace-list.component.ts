import { Component, OnInit, TemplateRef, Input } from '@angular/core';
import { BsModalService } from 'ngx-bootstrap/modal';
import { BsModalRef } from 'ngx-bootstrap/modal/bs-modal-ref.service';

import { WorkspaceService, Workspace } from '../../services/workspace.service';

@Component({
  selector: 'app-workspace-list',
  templateUrl: './workspace-list.component.html',
  styleUrls: ['./workspace-list.component.css']
})
export class WorkspaceListComponent implements OnInit {
  modalRef: BsModalRef;
  workspaces: Array<Workspace>;
  deletionCandidate: Workspace;
  newWorkspaceName: string;
  constructor(private workspaceService: WorkspaceService, private modalService: BsModalService) { }

  ngOnInit() {
    this.updateList();
  }
  updateList() {
    this.workspaceService.getWorkspaces().subscribe(workspaces => this.workspaces = workspaces);
  }
  deleteWorkspace(workspace: Workspace, confirmdeletion: TemplateRef<any>) {
    this.deletionCandidate = workspace;
    this.modalRef = this.modalService.show(confirmdeletion, { class: 'modal-sm' });
    //
  }
  confirmDeletion() {
    this.workspaceService.deleteWorkspace(this.deletionCandidate).subscribe(() => this.updateList());
    this.hideDeletionConfirm();
  }
  hideDeletionConfirm() {
    this.deletionCandidate = null;
    this.modalRef.hide();
    this.modalRef = null;
  }
  add(addDialog: TemplateRef<any>) {
    this.modalRef = this.modalService.show(addDialog, { class: 'modal-md' });
  }
  confirmAdd() {
    if (this.newWorkspaceName != '') {
      this.workspaceService.addWorkspace(this.newWorkspaceName).subscribe(workspace => {
        this.workspaces.push(workspace);
        this.hideCreationDialog();
      });
    }
  }
  hideCreationDialog() {
    this.newWorkspaceName = '';
    this.modalRef.hide();
    this.modalRef = null;
  }
}
