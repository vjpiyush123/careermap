/* CareerGuide — Main JavaScript */
'use strict';

/* ── Theme toggle ─────────────────────────────────────────── */
function _applyThemeIcon() {
    var icon = document.getElementById('themeIcon');
    if (!icon) return;
    var theme = document.documentElement.getAttribute('data-theme') || 'dark';
    icon.textContent = theme === 'dark' ? '\u2600\uFE0F' : '\uD83C\uDF19';
}

function toggleTheme() {
    var html = document.documentElement;
    var current = html.getAttribute('data-theme') || 'dark';
    var next = current === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('cg-theme', next);
    _applyThemeIcon();
}

document.addEventListener('DOMContentLoaded', function() {
    _applyThemeIcon();

    // Highlight current nav link
    var currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(function(link) {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // ── College Directory ──────────────────────────────────
    if (typeof ALL_COLLEGES !== 'undefined') {
        _initCollegeDirectory();
    }
});

/* ── College Directory Logic ──────────────────────────────── */

function _initCollegeDirectory() {
    var colleges = ALL_COLLEGES;
    var selected = [];      // indices for compare
    var debounceTimer = null;

    var elCards     = document.getElementById('cdCards');
    var elSearch    = document.getElementById('cdSearch');
    var elStream    = document.getElementById('cdStreamFilter');
    var elState     = document.getElementById('cdStateFilter');
    var elType      = document.getElementById('cdTypeFilter');
    var elBranch    = document.getElementById('cdBranchFilter');
    var elSort      = document.getElementById('cdSortBy');
    var elCount     = document.getElementById('cdResultCount');
    var elCompBtn   = document.getElementById('cdCompareBtn');
    var elCompCount = document.getElementById('cdCompareCount');
    var elReset     = document.getElementById('cdResetBtn');
    var elDetailOv  = document.getElementById('cdDetailOverlay');
    var elDetailC   = document.getElementById('cdDetailContent');
    var elDetailCl  = document.getElementById('cdDetailClose');
    var elCompOv    = document.getElementById('cdCompareOverlay');
    var elCompBody  = document.getElementById('cdCompareBody');
    var elCompClose = document.getElementById('cdCompareClose');

    function getFiltered() {
        var q = (elSearch.value || '').toLowerCase().trim();
        var stream = elState ? elStream.value : 'all';
        var state  = elState ? elState.value : 'all';
        var type   = elType  ? elType.value  : 'all';
        var branch = elBranch ? elBranch.value : 'all';

        var list = colleges.filter(function(c) {
            if (q) {
                var haystack = (c.name + ' ' + c.short_name + ' ' + c.city + ' ' + c.state + ' ' + c.institute_type).toLowerCase();
                if (haystack.indexOf(q) === -1) return false;
            }
            if (stream !== 'all') {
                // determine stream from institute_type heuristic
                var isEngg = ['IIT','NIT','IIIT','Private','State Govt','Deemed'].indexOf(c.institute_type) !== -1
                    && c.branches && c.branches.length > 0
                    && !c.branches[0].short_name.match(/^(MBBS|MD|MS|DM|MCh)/);
                if (stream === 'engineering' && !isEngg) return false;
                if (stream === 'medical' && isEngg) return false;
            }
            if (state !== 'all' && c.state !== state) return false;
            if (type !== 'all' && c.institute_type !== type) return false;
            if (branch !== 'all') {
                var hasBranch = (c.branches || []).some(function(b) {
                    return b.short_name === branch;
                });
                if (!hasBranch) return false;
            }
            return true;
        });

        // sort
        var sortKey = elSort ? elSort.value : 'ranking';
        list.sort(function(a, b) {
            switch (sortKey) {
                case 'fees_asc':         return a.avg_fees_lpa - b.avg_fees_lpa;
                case 'fees_desc':        return b.avg_fees_lpa - a.avg_fees_lpa;
                case 'placement_desc':   return b.avg_placement_lpa - a.avg_placement_lpa;
                case 'seats_desc':       return b.total_seats - a.total_seats;
                default:                 return (a.nirf_ranking || a.ranking || 999) - (b.nirf_ranking || b.ranking || 999);
            }
        });

        return list;
    }

    function renderCards() {
        var list = getFiltered();
        elCount.textContent = list.length + ' college' + (list.length !== 1 ? 's' : '');

        if (list.length === 0) {
            elCards.innerHTML = '<div class="cd-no-results">No colleges match your filters. Try adjusting your search.</div>';
            return;
        }

        var html = '';
        list.forEach(function(c, i) {
            var origIdx = colleges.indexOf(c);
            var isSelected = selected.indexOf(origIdx) !== -1;
            var branches = (c.branches || []).map(function(b) {
                return '<span class="cd-branch-tag">' + _esc(b.short_name) + '</span>';
            }).join('');

            html += '<div class="cd-card' + (isSelected ? ' cd-card-selected' : '') + '" data-idx="' + origIdx + '">'
                + '<div class="cd-card-top">'
                + '  <div>'
                + '    <div class="cd-card-name">' + _esc(c.short_name || c.name) + '</div>'
                + '    <div class="cd-card-short">' + _esc(c.name) + '</div>'
                + '  </div>'
                + '  <div class="cd-card-rank">'
                + '    <span class="cd-card-rank-label">NIRF</span>'
                + '    <span class="cd-card-rank-num">#' + (c.nirf_ranking || c.ranking || '–') + '</span>'
                + '  </div>'
                + '</div>'
                + '<div class="cd-card-meta">'
                + '  <span>' + _esc(c.city) + ', ' + _esc(c.state) + '</span>'
                + '  <span>' + _esc(c.institute_type) + '</span>'
                + '  <span>Est. ' + (c.established || '–') + '</span>'
                + '</div>'
                + '<div class="cd-card-branches">' + branches + '</div>'
                + '<div class="cd-card-stats">'
                + '  <div class="cd-stat"><span class="cd-stat-label">Fees</span><span class="cd-stat-value">\u20B9' + c.avg_fees_lpa + ' LPA</span></div>'
                + '  <div class="cd-stat"><span class="cd-stat-label">Avg Placement</span><span class="cd-stat-value">\u20B9' + c.avg_placement_lpa + ' LPA</span></div>'
                + '  <div class="cd-stat"><span class="cd-stat-label">Seats</span><span class="cd-stat-value">' + (c.total_seats || '–') + '</span></div>'
                + (c.naac_grade ? '  <div class="cd-stat"><span class="cd-stat-label">NAAC</span><span class="cd-stat-value">' + _esc(c.naac_grade) + '</span></div>' : '')
                + '</div>'
                + '<div class="cd-card-actions">'
                + '  <label class="cd-compare-check">'
                + '    <input type="checkbox" data-compare="' + origIdx + '"' + (isSelected ? ' checked' : '') + '>'
                + '    Compare'
                + '  </label>'
                + '  <button class="cd-view-btn" data-detail="' + origIdx + '">View Details</button>'
                + '</div>'
                + '</div>';
        });
        elCards.innerHTML = html;

        // Attach compare checkbox listeners directly after render
        elCards.querySelectorAll('[data-compare]').forEach(function(chk) {
            chk.addEventListener('change', function(e) {
                e.stopPropagation();
                var idx = parseInt(chk.getAttribute('data-compare'));
                if (chk.checked) {
                    if (selected.length < 3) { selected.push(idx); }
                    else { chk.checked = false; }
                } else {
                    selected = selected.filter(function(s) { return s !== idx; });
                }
                updateCompareUI();
                var card = chk.closest('.cd-card');
                if (card) {
                    if (chk.checked) card.classList.add('cd-card-selected');
                    else card.classList.remove('cd-card-selected');
                }
            });
        });
    }

    function updateCompareUI() {
        elCompCount.textContent = selected.length;
        elCompBtn.disabled = selected.length < 2;
    }

    // ── Event listeners ──────────────────────────────────────

    function onFilterChange() { renderCards(); }

    [elStream, elState, elType, elBranch, elSort].forEach(function(el) {
        if (el) el.addEventListener('change', onFilterChange);
    });

    if (elSearch) {
        elSearch.addEventListener('input', function() {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(renderCards, 200);
        });
    }

    if (elReset) {
        elReset.addEventListener('click', function() {
            elSearch.value = '';
            [elStream, elState, elType, elBranch].forEach(function(s) { if (s) s.value = 'all'; });
            if (elSort) elSort.value = 'ranking';
            selected = [];
            updateCompareUI();
            renderCards();
        });
    }

    // Card click delegation
    elCards.addEventListener('click', function(e) {
        // Skip if clicking inside the compare label area
        if (e.target.closest('.cd-compare-check')) return;

        var detailBtn = e.target.closest('[data-detail]');
        if (detailBtn) {
            showDetail(parseInt(detailBtn.getAttribute('data-detail')));
            return;
        }

        var card = e.target.closest('.cd-card');
        if (card && card.dataset.idx !== undefined) {
            showDetail(parseInt(card.dataset.idx));
        }
    });

    // ── Detail Panel ─────────────────────────────────────────

    function showDetail(idx) {
        var c = colleges[idx];
        if (!c) return;

        var badgesHtml = '';
        if (c.naac_grade) badgesHtml += '<span class="cd-badge cd-badge-accent">NAAC ' + _esc(c.naac_grade) + '</span>';
        if (c.nba_accredited) badgesHtml += '<span class="cd-badge cd-badge-success">NBA</span>';
        badgesHtml += '<span class="cd-badge cd-badge-warning">' + _esc(c.institute_type) + '</span>';

        var overviewGrid = ''
            + _detailStat('NIRF Ranking', '#' + (c.nirf_ranking || c.ranking || '–'))
            + _detailStat('Established', c.established || '–')
            + _detailStat('Total Seats', c.total_seats || '–')
            + _detailStat('Avg Fees', '\u20B9' + c.avg_fees_lpa + ' LPA')
            + _detailStat('Hostel Fees', '\u20B9' + (c.hostel_fees_per_year || '–') + ' LPA')
            + _detailStat('Avg Placement', '\u20B9' + c.avg_placement_lpa + ' LPA')
            + _detailStat('Median Placement', '\u20B9' + (c.median_placement_lpa || '–') + ' LPA')
            + _detailStat('Highest Package', '\u20B9' + (c.highest_placement_lpa || '–') + ' LPA')
            + _detailStat('Placement %', (c.placement_percentage || '–') + '%');

        var recruitersHtml = (c.top_recruiters || []).map(function(r) {
            return '<span class="cd-branch-tag">' + _esc(r) + '</span>';
        }).join('');

        var alumniHtml = (c.notable_alumni || []).map(function(a) {
            return '<span class="cd-branch-tag">' + _esc(a) + '</span>';
        }).join('');

        // Branches table
        var branchRows = (c.branches || []).map(function(b) {
            return '<tr>'
                + '<td><strong>' + _esc(b.short_name) + '</strong><br><span style="font-size:0.78rem;color:var(--text-muted)">' + _esc(b.name) + '</span></td>'
                + '<td>' + (b.ug_seats || '–') + '</td>'
                + '<td>' + (b.pg_seats || '–') + '</td>'
                + '<td>' + (b.dual_degree_seats || '–') + '</td>'
                + '<td>' + (b.avg_placement_lpa ? '\u20B9' + b.avg_placement_lpa + 'L' : '–') + '</td>'
                + '<td>' + (b.highest_placement_lpa ? '\u20B9' + b.highest_placement_lpa + 'L' : '–') + '</td>'
                + '<td>' + (b.placement_percentage ? b.placement_percentage + '%' : '–') + '</td>'
                + '</tr>';
        }).join('');

        // Cutoffs table
        var cutoffRows = (c.branches || []).filter(function(b) {
            return b.general_closing_rank > 0;
        }).map(function(b) {
            return '<tr>'
                + '<td><strong>' + _esc(b.short_name) + '</strong></td>'
                + '<td>' + _esc(b.cutoff_exam || '–') + '</td>'
                + '<td>' + (b.general_closing_rank || '–') + '</td>'
                + '<td>' + (b.obc_closing_rank || '–') + '</td>'
                + '<td>' + (b.sc_closing_rank || '–') + '</td>'
                + '<td>' + (b.st_closing_rank || '–') + '</td>'
                + '<td>' + (b.ews_closing_rank || '–') + '</td>'
                + '<td>' + (b.female_closing_rank || '–') + '</td>'
                + '</tr>';
        }).join('');

        // Course types table
        var courseRows = (c.course_types || []).map(function(ct) {
            return '<tr>'
                + '<td><strong>' + _esc(ct.name) + '</strong></td>'
                + '<td>' + ct.duration_years + ' yrs</td>'
                + '<td>' + _esc(ct.entrance_exam || '–') + '</td>'
                + '<td>' + (ct.fee_per_year_lpa ? '\u20B9' + ct.fee_per_year_lpa + ' LPA' : '–') + '</td>'
                + '<td style="font-size:0.8rem">' + _esc(ct.eligibility || '–') + '</td>'
                + '</tr>';
        }).join('');

        var html = ''
            + '<div class="cd-detail-header">'
            + '  <h2>' + _esc(c.name) + '</h2>'
            + '  <div class="cd-card-meta"><span>' + _esc(c.city) + ', ' + _esc(c.state) + '</span><span>Est. ' + (c.established || '–') + '</span>'
            + (c.website ? '<span><a href="' + _esc(c.website) + '" target="_blank" rel="noopener">Website \u2197</a></span>' : '')
            + '</div>'
            + '  <div class="cd-detail-badges">' + badgesHtml + '</div>'
            + '</div>'

            + '<div class="cd-detail-tabs" id="cdDetailTabs">'
            + '  <button class="cd-detail-tab active" data-dtab="dt-overview">Overview</button>'
            + '  <button class="cd-detail-tab" data-dtab="dt-branches">Branches</button>'
            + (cutoffRows ? '  <button class="cd-detail-tab" data-dtab="dt-cutoffs">Cutoffs</button>' : '')
            + '  <button class="cd-detail-tab" data-dtab="dt-courses">Courses</button>'
            + '  <button class="cd-detail-tab" data-dtab="dt-placements">Placements</button>'
            + '</div>'

            // Overview pane
            + '<div class="cd-detail-pane active" id="dt-overview">'
            + '  <div class="cd-detail-grid">' + overviewGrid + '</div>'
            + (recruitersHtml ? '<h4 style="margin:0.75rem 0 0.5rem;font-size:0.9rem;color:var(--text-secondary)">Top Recruiters</h4><div class="cd-card-branches">' + recruitersHtml + '</div>' : '')
            + (alumniHtml ? '<h4 style="margin:0.75rem 0 0.5rem;font-size:0.9rem;color:var(--text-secondary)">Notable Alumni</h4><div class="cd-card-branches">' + alumniHtml + '</div>' : '')
            + (c.fee_waiver_policy ? '<p style="margin-top:0.75rem;font-size:0.85rem;color:var(--text-secondary)"><strong>Fee Waiver:</strong> ' + _esc(c.fee_waiver_policy) + '</p>' : '')
            + '</div>'

            // Branches pane
            + '<div class="cd-detail-pane" id="dt-branches">'
            + '<div class="table-responsive"><table class="data-table">'
            + '<thead><tr><th>Branch</th><th>UG</th><th>PG</th><th>Dual</th><th>Avg Pkg</th><th>Max Pkg</th><th>Placed %</th></tr></thead>'
            + '<tbody>' + branchRows + '</tbody></table></div>'
            + '</div>'

            // Cutoffs pane
            + (cutoffRows
                ? '<div class="cd-detail-pane" id="dt-cutoffs">'
                + '<div class="table-responsive"><table class="data-table">'
                + '<thead><tr><th>Branch</th><th>Exam</th><th>General</th><th>OBC</th><th>SC</th><th>ST</th><th>EWS</th><th>Female</th></tr></thead>'
                + '<tbody>' + cutoffRows + '</tbody></table></div>'
                + '</div>'
                : '')

            // Courses pane
            + '<div class="cd-detail-pane" id="dt-courses">'
            + '<div class="table-responsive"><table class="data-table">'
            + '<thead><tr><th>Course</th><th>Duration</th><th>Entrance</th><th>Fee/yr</th><th>Eligibility</th></tr></thead>'
            + '<tbody>' + courseRows + '</tbody></table></div>'
            + '</div>'

            // Placements pane
            + '<div class="cd-detail-pane" id="dt-placements">'
            + '  <div class="cd-detail-grid">'
            + _detailStat('Avg Package', '\u20B9' + c.avg_placement_lpa + ' LPA')
            + _detailStat('Median Package', '\u20B9' + (c.median_placement_lpa || '–') + ' LPA')
            + _detailStat('Highest Package', '\u20B9' + (c.highest_placement_lpa || '–') + ' LPA')
            + _detailStat('Placement %', (c.placement_percentage || '–') + '%')
            + '  </div>'
            + (recruitersHtml ? '<h4 style="margin:0.5rem 0;font-size:0.9rem;color:var(--text-secondary)">Top Recruiters</h4><div class="cd-card-branches">' + recruitersHtml + '</div>' : '')
            + '</div>';

        elDetailC.innerHTML = html;
        elDetailOv.classList.add('open');
        document.body.style.overflow = 'hidden';

        // Detail tab switching
        var tabs = elDetailC.querySelectorAll('.cd-detail-tab');
        tabs.forEach(function(tab) {
            tab.addEventListener('click', function() {
                tabs.forEach(function(t) { t.classList.remove('active'); });
                tab.classList.add('active');
                elDetailC.querySelectorAll('.cd-detail-pane').forEach(function(p) { p.classList.remove('active'); });
                var target = elDetailC.querySelector('#' + tab.getAttribute('data-dtab'));
                if (target) target.classList.add('active');
            });
        });
    }

    function closeDetail() {
        elDetailOv.classList.remove('open');
        document.body.style.overflow = '';
    }

    elDetailCl.addEventListener('click', closeDetail);
    elDetailOv.addEventListener('click', function(e) {
        if (e.target === elDetailOv) closeDetail();
    });

    // ── Compare Modal ────────────────────────────────────────

    elCompBtn.addEventListener('click', function() {
        if (selected.length < 2) return;
        showCompare();
    });

    function showCompare() {
        var cols = selected.map(function(idx) { return colleges[idx]; });

        var rows = [
            ['College',       function(c) { return '<strong>' + _esc(c.short_name || c.name) + '</strong>'; }],
            ['City',          function(c) { return _esc(c.city + ', ' + c.state); }],
            ['Type',          function(c) { return _esc(c.institute_type); }],
            ['NIRF Rank',     function(c) { return '#' + (c.nirf_ranking || c.ranking || '–'); }],
            ['NAAC',          function(c) { return _esc(c.naac_grade || '–'); }],
            ['Established',   function(c) { return c.established || '–'; }],
            ['Total Seats',   function(c) { return c.total_seats || '–'; }],
            ['Fees (LPA)',    function(c) { return '\u20B9' + c.avg_fees_lpa; }],
            ['Avg Placement', function(c) { return '\u20B9' + c.avg_placement_lpa + ' LPA'; }],
            ['Median Pkg',    function(c) { return c.median_placement_lpa ? '\u20B9' + c.median_placement_lpa + ' LPA' : '–'; }],
            ['Highest Pkg',   function(c) { return c.highest_placement_lpa ? '\u20B9' + c.highest_placement_lpa + ' LPA' : '–'; }],
            ['Placement %',   function(c) { return c.placement_percentage ? c.placement_percentage + '%' : '–'; }],
            ['Branches',      function(c) {
                return (c.branches || []).map(function(b) { return b.short_name; }).join(', ');
            }],
            ['Top Recruiters', function(c) {
                return (c.top_recruiters || []).slice(0, 5).join(', ');
            }],
        ];

        var html = '<div class="table-responsive"><table class="data-table">';
        rows.forEach(function(row) {
            html += '<tr><th>' + row[0] + '</th>';
            cols.forEach(function(c) { html += '<td>' + row[1](c) + '</td>'; });
            html += '</tr>';
        });
        html += '</table></div>';

        elCompBody.innerHTML = html;
        elCompOv.classList.add('open');
        document.body.style.overflow = 'hidden';
    }

    function closeCompare() {
        elCompOv.classList.remove('open');
        document.body.style.overflow = '';
    }

    elCompClose.addEventListener('click', closeCompare);
    elCompOv.addEventListener('click', function(e) {
        if (e.target === elCompOv) closeCompare();
    });

    // ── Escape key closes modals ─────────────────────────────
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            if (elCompOv.classList.contains('open')) closeCompare();
            else if (elDetailOv.classList.contains('open')) closeDetail();
        }
    });

    // ── Helpers ──────────────────────────────────────────────

    function _detailStat(label, value) {
        return '<div class="cd-detail-stat">'
            + '<div class="cd-stat-label">' + label + '</div>'
            + '<div class="cd-stat-value">' + value + '</div>'
            + '</div>';
    }

    // initial render
    renderCards();
}

function _esc(s) {
    if (!s) return '';
    var d = document.createElement('div');
    d.textContent = String(s);
    return d.innerHTML;
}
