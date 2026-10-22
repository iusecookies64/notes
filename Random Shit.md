  ### 2. How to Know if a Linux PC Has Malware (Key Symptoms)                                                                                                                              
                                                                                                                                                                                           
  Watch for these common red flags:                                                                                                                                                        
                                                                                                                                                                                           
  1. Unexplained Resource Spikes:                                                                                                                                                          
      • The CPU/GPU fans spin up aggressively while the computer is idle (common with cryptominers).                                                                                       
      • Check with:                                                                                                                                                                        
        top                                                                                                                                                                                
        # or                                                                                                                                                                               
        glances                                                                                                                                                                            
                                                                                                                                                                                           
  2. Rogue Processes Running from Temporary Directories:                                                                                                                                   
      • Malware on Linux often drops payloads in /tmp, /var/tmp, or /dev/shm to bypass file permissions.                                                                                   
      • Quick check command:                                                                                                                                                               
        ls -l /proc/*/exe 2>/dev/null | grep -E 'deleted|/tmp|/dev/shm'                                                                                                                    
                                                                                                                                                                                           
  3. Suspicious Outbound Network Connections:                                                                                                                                              
      • Periodic or constant TCP connections to unfamiliar public IP addresses or high, non-standard ports.                                                                                
      • Quick check command:
        ss -tunp state established
  
  4. Unexpected Autostart Items:
      • Malicious scripts added to your crontab (crontab -l), ~/.config/autostart/, or ~/.bashrc.
  5. Browser Anomalies:
      • Unwanted browser extensions appearing without your consent, search engine redirects, or unusual certificate warnings.
  
  ──────
  ### 3. Recommended Tools for Deep On-Demand Scans
  
  If you ever suspect malware or want automated scanning, install these reputable tools:
  
  #### A. Scan Files for Viruses & Trojans (ClamAV)
  
    sudo apt update && sudo apt install -y clamav
    sudo freshclam
    clamscan -r -i ~/Downloads
  
  #### B. Scan for Rootkits & Backdoors (rkhunter & chkrootkit)
  
    sudo apt install -y rkhunter chkrootkit
    sudo rkhunter --update
    sudo rkhunter --check --sk
  
  #### C. System Security Audit (Lynis)
  
    sudo apt install -y lynis
    sudo lynis audit system
  
  #### D. Enable the Firewall (UFW)
  
  Ensure your local firewall is active to block unsolicited inbound connections:
  
    sudo ufw enable
    sudo ufw status