// ============================================================
// TCKC THREAT TRACKER - REFERENCE SECTIONS CODE EXTRACTION
// For: "View Threat Level Classification Criteria"
//      "View Definitions of Cultural Resources"  
//      "View Agency Organizational Charts"
// ============================================================

// ============================================================
// REQUIRED IMPORTS (React)
// ============================================================
import React, { useState } from 'react';
import { AlertCircle, Eye, Building2, ChevronUp, ChevronDown } from 'lucide-react';

// ============================================================
// BRAND COLORS
// ============================================================
const brand = {
  cream: '#FFF8E7',
  black: '#1A1A1A',
  gold: '#C4A052'
};

// ============================================================
// DATA CONSTANT 1: THREAT_LEVEL_CRITERIA
// Used by: "View Threat Level Classification Criteria"
// ============================================================
const THREAT_LEVEL_CRITERIA = {
  CRITICAL: {
    level: 'CRITICAL',
    icon: '🔴',
    label: 'Critical Risk',
    color: '#991B1B',
    bgColor: '#FEE2E2',
    description: 'Severe threat to cultural resources and communities',
    criteria: [
      'Significantly harms communities\' access to and enjoyment of cultural places and treasures',
      'Defunds or eliminates programs supporting cultural practices and heritage preservation',
      'Actively discriminates against people, especially members of cultural communities',
      'Threatens irreversible damage to cultural resources, sacred sites, or traditional practices',
      'Eliminates federal protections for cultural heritage or Indigenous rights'
    ]
  },
  MODERATE: {
    level: 'MODERATE',
    icon: '🟡',
    label: 'Moderate Risk',
    color: '#CA8A04',
    bgColor: '#FEF9C3',
    description: 'Notable concern for cultural resources and communities',
    criteria: [
      'Reduces or limits communities\' access to cultural places and treasures',
      'Decreases funding or resources for cultural practices and heritage programs',
      'Discourages participation in or support for cultural activities',
      'Creates administrative barriers to cultural preservation efforts',
      'Weakens existing protections without fully eliminating them'
    ]
  },
  PROTECTIVE: {
    level: 'PROTECTIVE',
    icon: '🟢',
    label: 'Protective',
    color: '#065F46',
    bgColor: '#D1FAE5',
    description: 'Supports and strengthens cultural resources and communities',
    criteria: [
      'Augments or increases communities\' access to cultural places and treasures',
      'Provides funding or resources to support cultural practices and heritage preservation',
      'Raises general public awareness and support for cultural communities',
      'Strengthens legal protections for cultural resources, sacred sites, or traditional practices',
      'Promotes inclusion and recognition of diverse cultural communities'
    ]
  }
};

// ============================================================
// DATA CONSTANT 2: CULTURAL_HERITAGE_CATEGORIES
// Used by: "View Definitions of Cultural Resources"
// ============================================================
const CULTURAL_HERITAGE_CATEGORIES = {
  TANGIBLE: {
    name: 'Tangible Cultural Heritage',
    description: 'Physical, material expressions of cultural heritage that can be touched, seen, and preserved',
    color: '#7C3AED',
    bgColor: '#EDE9FE',
    resources: ['places', 'treasures']
  },
  INTANGIBLE: {
    name: 'Intangible Cultural Heritage',
    description: 'Living expressions of cultural heritage passed through generations, including traditions, knowledge, and skills',
    color: '#0891B2',
    bgColor: '#CFFAFE',
    resources: ['people', 'practices']
  }
};

// ============================================================
// DATA CONSTANT 3: FOUR_PS_FRAMEWORK
// Used by: "View Definitions of Cultural Resources"
// ============================================================
const FOUR_PS_FRAMEWORK = {
  people: {
    id: 'people',
    label: 'People',
    icon: '👥',
    category: 'INTANGIBLE',
    shortDescription: 'Cultural community members and heritage bearers',
    fullDescription: 'Encompasses the human dimension of intangible cultural heritage-the individuals and communities who create, maintain, and transmit cultural traditions.',
    includes: [
      'Cultural practitioners, artists, and tradition bearers',
      'Indigenous peoples and tribal community members',
      'Immigrant and diaspora communities',
      'Religious and spiritual leaders performing cultural functions',
      'Language speakers and teachers of indigenous and heritage languages',
      'Elders and knowledge keepers',
      'Cultural organization staff and museum professionals'
    ],
    protections: [
      'Free expression of cultural and religious practices',
      'Immigration agreements supporting cultural communities',
      'Anti-discrimination protections for cultural community members',
      'Support for indigenous language preservation and revitalization',
      'Recognition of specialized cultural and religious functions',
      'Funding for cultural education and transmission programs'
    ]
  },
  places: {
    id: 'places',
    label: 'Places',
    icon: '📍',
    category: 'TANGIBLE',
    shortDescription: 'Historic sites and cultural landscapes',
    fullDescription: 'Encompasses all tangible cultural heritage tied to specific locations-the physical spaces where cultural heritage exists and cultural practices occur.',
    includes: [
      'Historic sites and districts',
      'Sacred sites and ceremonial grounds',
      'National parks, monuments, and heritage areas',
      'Archaeological sites and ancestral lands',
      'Cultural landscapes and traditional use areas',
      'Museums, libraries, and archives',
      'Historic buildings and structures',
      'Burial grounds and memorial sites'
    ],
    protections: [
      'National Historic Preservation Act protections',
      'Section 106 review for federal undertakings',
      'Tribal consultation requirements',
      'National Register of Historic Places listings',
      'UNESCO World Heritage Site designations',
      'NAGPRA protections for sacred sites'
    ]
  },
  practices: {
    id: 'practices',
    label: 'Practices',
    icon: '🎨',
    category: 'INTANGIBLE',
    shortDescription: 'Living traditions and cultural expressions',
    fullDescription: 'Encompasses intangible cultural heritage-the living expressions, knowledge, and skills transmitted through generations within communities.',
    includes: [
      'Traditional arts, crafts, and artistic expressions',
      'Oral traditions, storytelling, and folklore',
      'Music, dance, and performing arts',
      'Religious and spiritual ceremonies',
      'Traditional ecological knowledge',
      'Foodways and culinary traditions',
      'Indigenous languages and dialects',
      'Subsistence practices and traditional lifeways',
      'Healing traditions and traditional medicine'
    ],
    protections: [
      'First Amendment free expression protections',
      'Religious Freedom Restoration Act',
      'American Indian Religious Freedom Act',
      'Native American Languages Act',
      'NEA/NEH funding for traditional arts',
      'Smithsonian Folklife programming'
    ]
  },
  treasures: {
    id: 'treasures',
    label: 'Treasures',
    icon: '💎',
    category: 'TANGIBLE',
    shortDescription: 'Cultural objects and material heritage',
    fullDescription: 'Encompasses all tangible cultural heritage in the form of movable objects-the physical artifacts and materials that embody cultural significance.',
    includes: [
      'Museum collections and cultural artifacts',
      'Artworks, sculptures, and visual art',
      'Manuscripts, documents, and archives',
      'Sacred objects and ceremonial items',
      'Archaeological collections',
      'Ancestral remains and funerary objects',
      'Traditional regalia and clothing',
      'Musical instruments and craft objects',
      'Photographs, recordings, and audiovisual materials',
      'Real property with cultural significance'
    ],
    protections: [
      'NAGPRA repatriation requirements',
      'Cultural property import/export restrictions',
      'Museum collection care standards',
      'Copyright and intellectual property protections',
      'Archival preservation standards',
      'Provenance and ownership documentation'
    ]
  }
};

// ============================================================
// DATA CONSTANT 4: AGENCY_REGISTRY
// Used by: "View Agency Organizational Charts"
// ============================================================
const AGENCY_REGISTRY = {
  DOI: { code: 'DOI', name: 'Department of the Interior', subAgencies: [
    { code: 'NPS', name: 'National Park Service' },
    { code: 'BLM', name: 'Bureau of Land Management' },
    { code: 'BIA', name: 'Bureau of Indian Affairs' },
    { code: 'BOR', name: 'Bureau of Reclamation' },
    { code: 'FWS', name: 'U.S. Fish and Wildlife Service' },
    { code: 'USGS', name: 'U.S. Geological Survey' },
    { code: 'OSM', name: 'Office of Surface Mining' },
    { code: 'BOEM', name: 'Bureau of Ocean Energy Management' },
    { code: 'BSEE', name: 'Bureau of Safety and Environmental Enforcement' },
    { code: 'ONRR', name: 'Office of Natural Resources Revenue' }
  ]},
  EPA: { code: 'EPA', name: 'Environmental Protection Agency', subAgencies: [
    { code: 'OAR', name: 'Office of Air and Radiation' },
    { code: 'OW', name: 'Office of Water' },
    { code: 'OLEM', name: 'Office of Land and Emergency Management' },
    { code: 'OCSPP', name: 'Office of Chemical Safety and Pollution Prevention' },
    { code: 'OECA', name: 'Office of Enforcement and Compliance Assurance' },
    { code: 'OEJ', name: 'Office of Environmental Justice' },
    { code: 'REGIONS', name: 'Regional Offices (1-10)' }
  ]},
  NOAA: { code: 'NOAA', name: 'National Oceanic and Atmospheric Administration', subAgencies: [
    { code: 'NMFS', name: 'National Marine Fisheries Service' },
    { code: 'NOS', name: 'National Ocean Service' },
    { code: 'NWS', name: 'National Weather Service' },
    { code: 'OAR', name: 'Office of Oceanic and Atmospheric Research' },
    { code: 'NESDIS', name: 'National Environmental Satellite, Data, and Information Service' },
    { code: 'OMAO', name: 'Office of Marine and Aviation Operations' }
  ]},
  NARA: { code: 'NARA', name: 'National Archives and Records Administration', subAgencies: [
    { code: 'OFR', name: 'Office of the Federal Register' },
    { code: 'NHPRC', name: 'National Historical Publications and Records Commission' },
    { code: 'PL', name: 'Presidential Libraries' },
    { code: 'OGIS', name: 'Office of Government Information Services' },
    { code: 'ISOO', name: 'Information Security Oversight Office' }
  ]},
  LOC: { code: 'LOC', name: 'Library of Congress', subAgencies: [
    { code: 'CRS', name: 'Congressional Research Service' },
    { code: 'USCO', name: 'U.S. Copyright Office' },
    { code: 'AFC', name: 'American Folklife Center' },
    { code: 'CFB', name: 'Center for the Book' },
    { code: 'FEDLINK', name: 'Federal Library and Information Network' },
    { code: 'NLS', name: 'National Library Service for the Blind' },
    { code: 'VHP', name: 'Veterans History Project' }
  ]},
  SMITHSONIAN: { code: 'SMITHSONIAN', name: 'Smithsonian Institution', subAgencies: [
    { code: 'NMAH', name: 'National Museum of American History' },
    { code: 'NMNH', name: 'National Museum of Natural History' },
    { code: 'NMAAHC', name: 'National Museum of African American History and Culture' },
    { code: 'NMAI', name: 'National Museum of the American Indian' },
    { code: 'NASM', name: 'National Air and Space Museum' },
    { code: 'SAAM', name: 'Smithsonian American Art Museum' },
    { code: 'NPG', name: 'National Portrait Gallery' },
    { code: 'HMSG', name: 'Hirshhorn Museum and Sculpture Garden' },
    { code: 'NMAL', name: 'National Museum of the American Latino' },
    { code: 'SAWHM', name: 'Smithsonian American Women\'s History Museum' },
    { code: 'ACM', name: 'Anacostia Community Museum' },
    { code: 'CHSDM', name: 'Cooper Hewitt, Smithsonian Design Museum' },
    { code: 'FSG', name: 'Freer Gallery of Art and Arthur M. Sackler Gallery' },
    { code: 'RENWICK', name: 'Renwick Gallery' },
    { code: 'NPM', name: 'National Postal Museum' },
    { code: 'AIB', name: 'Arts and Industries Building' },
    { code: 'NZCBI', name: 'National Zoo and Conservation Biology Institute' },
    { code: 'SLA', name: 'Smithsonian Libraries and Archives' },
    { code: 'AAA', name: 'Archives of American Art' },
    { code: 'STRI', name: 'Smithsonian Tropical Research Institute' },
    { code: 'SERC', name: 'Smithsonian Environmental Research Center' },
    { code: 'SAO', name: 'Smithsonian Astrophysical Observatory' },
    { code: 'MCI', name: 'Museum Conservation Institute' }
  ]},
  IMLS: { code: 'IMLS', name: 'Institute of Museum and Library Services', subAgencies: [
    { code: 'OMS', name: 'Office of Museum Services' },
    { code: 'OLS', name: 'Office of Library Services' },
    { code: 'ODL', name: 'Office of Digital and Library Innovation' },
    { code: 'OGPM', name: 'Office of Grants Policy and Management' }
  ]},
  NEA: { code: 'NEA', name: 'National Endowment for the Arts', subAgencies: [
    { code: 'GAP', name: 'Grants for Arts Projects' },
    { code: 'CA', name: 'Challenge America' },
    { code: 'CWF', name: 'Creative Writing Fellowships' },
    { code: 'RA', name: 'Research & Analysis' },
    { code: 'AEP', name: 'Arts Education Partnership' }
  ]},
  NEH: { code: 'NEH', name: 'National Endowment for the Humanities', subAgencies: [
    { code: 'DRP', name: 'Division of Research Programs' },
    { code: 'DEP', name: 'Division of Education Programs' },
    { code: 'DPP', name: 'Division of Public Programs' },
    { code: 'DPA', name: 'Division of Preservation and Access' },
    { code: 'OCG', name: 'Office of Challenge Grants' },
    { code: 'FSP', name: 'Federal/State Partnership' }
  ]},
  KENNEDY: { code: 'KENNEDY', name: 'John F. Kennedy Center for the Performing Arts', subAgencies: [
    { code: 'NSO', name: 'National Symphony Orchestra' },
    { code: 'WNO', name: 'Washington National Opera' },
    { code: 'VSA', name: 'VSA and Accessibility' },
    { code: 'KCED', name: 'Kennedy Center Education' }
  ]},
  CPB: { code: 'CPB', name: 'Corporation for Public Broadcasting', subAgencies: [
    { code: 'PBS', name: 'Public Broadcasting Service' },
    { code: 'NPR', name: 'National Public Radio' },
    { code: 'RTL', name: 'Ready To Learn' },
    { code: 'CSG', name: 'Community Service Grants' }
  ]},
  ED: { code: 'ED', name: '* Department of Education', subAgencies: [
    { code: 'OCR', name: 'Office for Civil Rights' },
    { code: 'OESE', name: 'Office of Elementary and Secondary Education' },
    { code: 'OPE', name: 'Office of Postsecondary Education' },
    { code: 'OSERS', name: 'Office of Special Education and Rehabilitative Services' },
    { code: 'FSA', name: 'Federal Student Aid' },
    { code: 'IES', name: 'Institute of Education Sciences' },
    { code: 'OELA', name: 'Office of English Language Acquisition' },
    { code: 'WHIHBCU', name: 'White House Initiative on HBCUs' }
  ]},
  HHS: { code: 'HHS', name: '* Department of Health and Human Services', subAgencies: [
    { code: 'ANA', name: 'Administration for Native Americans' },
    { code: 'OMH', name: 'Office of Minority Health' },
    { code: 'IHS', name: 'Indian Health Service' },
    { code: 'ACF', name: 'Administration for Children and Families' },
    { code: 'OCR', name: 'Office for Civil Rights' }
  ]},
  USDA: { code: 'USDA', name: '* Department of Agriculture', subAgencies: [
    { code: 'FS', name: 'Forest Service' },
    { code: 'NRCS', name: 'Natural Resources Conservation Service' },
    { code: 'RD', name: 'Rural Development' },
    { code: 'OTR', name: 'Office of Tribal Relations' }
  ]},
  DHS: { code: 'DHS', name: '** Department of Homeland Security', subAgencies: [
    { code: 'ICE', name: 'Immigration and Customs Enforcement' },
    { code: 'CBP', name: 'Customs and Border Protection' },
    { code: 'USCIS', name: 'U.S. Citizenship and Immigration Services' },
    { code: 'SEVP', name: 'Student and Exchange Visitor Program' },
    { code: 'EOIR', name: 'Executive Office for Immigration Review' }
  ]},
  STATE: { code: 'STATE', name: '** Department of State', subAgencies: [
    { code: 'CA/VO', name: 'Bureau of Consular Affairs - Visa Office' },
    { code: 'PRM', name: 'Bureau of Population, Refugees, and Migration' },
    { code: 'DRL', name: 'Bureau of Democracy, Human Rights, and Labor' }
  ]},
  DOJ: { code: 'DOJ', name: '** Department of Justice', subAgencies: [
    { code: 'EOIR', name: 'Executive Office for Immigration Review' },
    { code: 'CRT', name: 'Civil Rights Division' },
    { code: 'OLC', name: 'Office of Legal Counsel' }
  ]}
};

// ============================================================
// REACT COMPONENT: ReferenceSections
// Contains all three collapsible sections
// ============================================================
const ReferenceSections = () => {
  // State for toggling each section
  const [showCriteria, setShowCriteria] = useState(false);
  const [showFramework, setShowFramework] = useState(false);
  const [showAgencies, setShowAgencies] = useState(false);

  return (
    <div className="space-y-4">
      
      {/* ============================================================ */}
      {/* SECTION 1: Threat Level Classification Criteria */}
      {/* ============================================================ */}
      <div className="mb-4">
        <button 
          onClick={() => setShowCriteria(!showCriteria)}
          className="text-xs flex items-center gap-1 opacity-60 hover:opacity-100 transition-opacity"
          style={{ fontFamily: 'system-ui, sans-serif' }}
        >
          <AlertCircle className="w-3 h-3" />
          {showCriteria ? 'Hide' : 'View'} Threat Level Classification Criteria
          {showCriteria ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
        </button>
        
        {showCriteria && (
          <div className="mt-3 grid md:grid-cols-3 gap-3">
            {Object.entries(THREAT_LEVEL_CRITERIA).map(([key, data]) => (
              <div 
                key={key} 
                className="rounded-lg p-3 border-l-4"
                style={{ backgroundColor: data.bgColor, borderLeftColor: data.color }}
              >
                <div className="flex items-center gap-2 mb-2">
                  <span className="text-lg">{data.icon}</span>
                  <span className="font-semibold text-sm" style={{ color: data.color }}>{data.label}</span>
                </div>
                <p className="text-xs opacity-80 mb-2">{data.description}</p>
                <ul className="space-y-1">
                  {data.criteria.map((criterion, idx) => (
                    <li key={idx} className="text-xs flex items-start gap-1">
                      <span className="mt-1">•</span>
                      <span>{criterion}</span>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* ============================================================ */}
      {/* SECTION 2: Definitions of Cultural Resources */}
      {/* ============================================================ */}
      <div className="mb-4">
        <button 
          onClick={() => setShowFramework(!showFramework)}
          className="text-xs flex items-center gap-1 opacity-60 hover:opacity-100 transition-opacity"
          style={{ fontFamily: 'system-ui, sans-serif' }}
        >
          <Eye className="w-3 h-3" />
          {showFramework ? 'Hide' : 'View'} Definitions of Cultural Resources
          {showFramework ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
        </button>
        
        {showFramework && (
          <div className="mt-3 space-y-4">
            {/* Heritage Categories Overview */}
            <div className="grid md:grid-cols-2 gap-3">
              {Object.entries(CULTURAL_HERITAGE_CATEGORIES).map(([key, cat]) => (
                <div 
                  key={key}
                  className="rounded-lg p-3 border-l-4"
                  style={{ backgroundColor: cat.bgColor, borderLeftColor: cat.color }}
                >
                  <h4 className="font-semibold text-sm mb-1" style={{ color: cat.color }}>{cat.name}</h4>
                  <p className="text-xs opacity-80 mb-2">{cat.description}</p>
                  <div className="flex gap-2">
                    {cat.resources.map(r => (
                      <span key={r} className="text-xs px-2 py-1 rounded-full bg-white">
                        {FOUR_PS_FRAMEWORK[r].icon} {FOUR_PS_FRAMEWORK[r].label}
                      </span>
                    ))}
                  </div>
                </div>
              ))}
            </div>

            {/* Detailed Framework - The Four P's */}
            <div className="grid md:grid-cols-2 gap-3">
              {Object.entries(FOUR_PS_FRAMEWORK).map(([key, resource]) => {
                const category = CULTURAL_HERITAGE_CATEGORIES[resource.category];
                return (
                  <div 
                    key={key}
                    className="rounded-lg p-4 bg-white border-2"
                    style={{ borderColor: category.color + '40' }}
                  >
                    <div className="flex items-center gap-2 mb-2">
                      <span className="text-2xl">{resource.icon}</span>
                      <div>
                        <h4 className="font-semibold text-sm">{resource.label}</h4>
                        <span 
                          className="text-xs px-2 py-0.5 rounded-full"
                          style={{ backgroundColor: category.bgColor, color: category.color }}
                        >
                          {resource.category === 'TANGIBLE' ? 'Tangible Heritage' : 'Intangible Heritage'}
                        </span>
                      </div>
                    </div>
                    <p className="text-xs opacity-80 mb-3">{resource.fullDescription}</p>
                    
                    <div className="mb-3">
                      <h5 className="font-semibold text-xs mb-1">Includes:</h5>
                      <ul className="grid grid-cols-1 gap-0.5">
                        {resource.includes.slice(0, 5).map((item, idx) => (
                          <li key={idx} className="text-xs flex items-start gap-1">
                            <span className="opacity-40">•</span>
                            <span className="opacity-70">{item}</span>
                          </li>
                        ))}
                        {resource.includes.length > 5 && (
                          <li className="text-xs opacity-50 italic">
                            + {resource.includes.length - 5} more...
                          </li>
                        )}
                      </ul>
                    </div>
                    
                    <div>
                      <h5 className="font-semibold text-xs mb-1">Key Protections:</h5>
                      <ul className="grid grid-cols-1 gap-0.5">
                        {resource.protections.slice(0, 3).map((item, idx) => (
                          <li key={idx} className="text-xs flex items-start gap-1">
                            <span className="opacity-40">•</span>
                            <span className="opacity-70">{item}</span>
                          </li>
                        ))}
                        {resource.protections.length > 3 && (
                          <li className="text-xs opacity-50 italic">
                            + {resource.protections.length - 3} more...
                          </li>
                        )}
                      </ul>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        )}
      </div>

      {/* ============================================================ */}
      {/* SECTION 3: Agency Organizational Charts */}
      {/* ============================================================ */}
      <div className="mb-4">
        <button 
          onClick={() => setShowAgencies(!showAgencies)}
          className="text-xs flex items-center gap-1 opacity-60 hover:opacity-100 transition-opacity"
          style={{ fontFamily: 'system-ui, sans-serif' }}
        >
          <Building2 className="w-3 h-3" />
          {showAgencies ? 'Hide' : 'View'} Agency Organizational Charts
          {showAgencies ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
        </button>
        
        {showAgencies && (
          <div className="mt-3 grid md:grid-cols-2 lg:grid-cols-3 gap-3">
            {Object.entries(AGENCY_REGISTRY).map(([key, agency]) => (
              <div 
                key={key}
                className="rounded-lg p-3 bg-white border"
                style={{ borderColor: brand.black + '20' }}
              >
                <h4 className="font-semibold text-sm mb-2" style={{ color: brand.black }}>
                  <span className="font-bold">{agency.code}</span> - {agency.name} <span className="opacity-50">({agency.subAgencies?.length || 0})</span>
                </h4>
                {agency.subAgencies && agency.subAgencies.length > 0 && (
                  <ul className="space-y-1">
                    {agency.subAgencies.map((sub, idx) => (
                      <li key={idx} className="text-xs flex items-start gap-1">
                        <span className="opacity-40">•</span>
                        <span>
                          <span className="font-semibold">{sub.code}</span>
                          <span className="opacity-70"> - {sub.name}</span>
                        </span>
                      </li>
                    ))}
                  </ul>
                )}
              </div>
            ))}
          </div>
        )}
      </div>

    </div>
  );
};

export default ReferenceSections;

// ============================================================
// USAGE INSTRUCTIONS
// ============================================================
/*
1. Install dependencies:
   npm install react lucide-react

2. If using Tailwind CSS, ensure your tailwind.config.js includes
   the necessary color and spacing utilities.

3. Import and use in your app:
   
   import ReferenceSections from './tckc-reference-sections-code';
   
   function App() {
     return (
       <div className="p-4">
         <ReferenceSections />
       </div>
     );
   }

4. The component uses:
   - Lucide React icons (AlertCircle, Eye, Building2, ChevronUp, ChevronDown)
   - Tailwind CSS classes for styling
   - React useState for toggle functionality

5. Customize colors by modifying the brand object and color values
   in the data constants.
*/
